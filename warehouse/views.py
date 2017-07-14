from django.shortcuts import render
import boto3
from datetime import datetime
from datetime import date as date_lib
from operator import getitem
import whois, openpyxl, re, os
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import dns.resolver

# Create your views here.

import importaws2
import acc_keys
from importaws2 import create_date, flo

from .models import AWS, AWS_files, AWS_Budget, Domain, Budget_Detail, High_Level_Budget, GL
from .forms import UploadFileForm, AddDomainForm

def boom(request):
    d = AWS.objects.all()
    d.delete()
    d = AWS_files.objects.all()
    d.delete()
    return render(request, 'warehouse/index.html')

def parse_acutals(f):
    with open('/home/ericoak/collywop/files/f.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


    wb = openpyxl.load_workbook('/home/ericoak/collywop/files/f.xlsx')
    budget = wb.get_sheet_by_name('Budget')
    bug_det = wb.get_sheet_by_name('BudgetDetail')
    gl = wb.get_sheet_by_name('GeneralLedgerReport')

    #work through budget sheet
    m_row = budget.max_row
    r = 1
    while r <= m_row:
        co = budget['A'+str(r)].value
        na = budget['B'+str(r)].value
        try:
            q = High_Level_Budget.objects.get(code=co)
            continue
        except:
            q = High_Level_Budget(code=co,name=na)
            q.save()
        r = r + 1

    # parse budget detail
    monthconvert = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    re_date = re.compile(r'(\w{3})-(\d{2})')

    m_row = bug_det.max_row
    r = 1
    while r <= m_row:
        r_d = int(bug_det['B'+str(r)].value)
        bug = bug_det['A'+str(r)].value
        acc = bug_det['C'+str(r)].value
        desc = bug_det['D'+str(r)].value
        co = round(float(bug_det['E'+str(r)].value),3)
        q_co = Budget.objects.get(code=co)
        co = q_co
        mo = bug_det['G'+str(r)].value
        mor = re_date.search(mo)
        mo = date(int('20'+str(mor.group(2))), mor.group(1), 1)
        amo = round(float(bug_det['H'+str(r)].value),2)
        try:
            q = Budget_Detail.objects.get(r_id=r_d)
            q.budget = bug
            q.account = acc
            q.description = desc
            q.code = co
            q.month = mo
            q.ammount = amo
            q.save()
        except:
            q = Budget_Detail(budget=bug, account=acc, description=desc, code=co, month=mo, ammount=amo, r_id=r_d)
            q.save()
        r = r + 1

    #parse GL
    m_row = gl.max_row
    r = 1
    while r<= m_row:
        post = gl['A'+str(r)].value
        mor = re_date.search(post)
        post = date(int('20'+str(mor.group(2))), mor.group(1), 1)
        r_d = int(gl['C'+str(r)].value)
        inv_d = gl['B'+str(r)].value
        mor = re_date.search(inv_d)
        inv_d = date(int('20'+str(mor.group(2))), mor.group(1), 1)
        gl_id = gl['D'+str(r)].value
        ven = gl['E'+str(r)].value
        inv = gl['F'+str(r)].value
        mem = gl['G'+str(r)].value
        co_str = gl['H'+str(r)].value
        cat = gl['I'+str(r)].value
        cl1 = gl['J'+str(r)].value
        cl2 = gl['K'+str(r)].value
        com = gl['L'+str(r)].value
        own = gl['M'+str(r)].value
        acc = gl['N'+str(r)].value
        dept_num = gl['O'+str(r)].value
        dept = gl['P'+str(r)].value
        co = round(float(gl['Q'+str(r)].value),3)
        q_co = Budget.objects.get(code=co)
        co = q_co
        loc_name = gl['R'+str(r)].value
        loc = gl['S'+str(r)].value
        proj_name = gl['T'+str(r)].value
        txn_no = gl['U'+str(r)].value
        jnl = gl['V'+str(r)].value
        curr = gl['W'+str(r)].value
        money = round(float(gl['X'+str(r)].value),2)
        try:
            q = GL.objects.get(r_id=r_d)
            q.posted = post
            q.inv_date = inv_d
            q.gl_id = gl_id
            q.vendor = ven
            q.invoice = inv
            q.memo = mem
            q.cost_structure = co_str
            q.category = cat
            q.class_1 = cl1
            q.class_2 = cl2
            q.comments = com
            q.owner = own
            q.account = acc
            q.dept_num = dept_num
            q.dept = dept
            q.code = co
            q.location_name = loc_name
            q.location = loc
            q.project_name = proj_name
            q.txn_no = txn_no
            q.jnl = jnl
            q.curr = curr
            q.money = money
            q.save()
        except:
            q = GL(posted = post, inv_date = inv_d, gl_id = gl_id, vendor = ven, invoice = inv, memo = mem, cost_structure = co_str, category = cat, class_1 = cl1, class_2 = cl2, comments = com, owner = own, account = acc,
                   dept_num = dept_num, dept = dept, code = co, location_name = loc_name, location = loc, project_name = proj_name, txn_no = txn_no, jnl = jnl, curr = curr, money = money, r_id= r_d)
            q.save()
        r = r + 1

def load_files(request):
    if request.method != 'POST':
        form = UploadFileForm()
    else:
        form = UploadFileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('warehouse/index.html')
    context = {'form': form}
    return render(request, 'warehouse/upload.html', context)

def del_cur_month(request):
    #figure out what day and month it is
    date = date_lib.today()
    year = date.year
    month = date.month
    if int(month) <10:
        month = '0'+str(month)
    day = date.day
    #pull key and formated month for current month
    key = importaws2.find_key(month, year)
    fmonth = importaws2.month(month, year)
    m = AWS_files.objects.get(month=fmonth)
    d = AWS.objects.filter(key=m.key)
    d.delete()
    return render(request, 'warehouse/index.html')

def aws_dash(request):
    #pull Data
    d = AWS.objects.all()
    #filter for EC2
    ec2 = d.filter(product_ProductName='Amazon Elastic Compute Cloud', )
    #filter for instances
    #find current date
    #filer for day
    #get the last


    return render(request, 'warehouse/aws_dash.html')

def importaws(request, tog):
    #figure out what day and month it is
    date = date_lib.today()
    year = date.year
    month = date.month
    if int(month) <10:
        month = '0'+str(month)
    day = date.day
    if int(tog) == 1:
        day = 1
    #pull key and formated month for current month
    key = importaws2.find_key(month, year)
    fmonth = importaws2.month(month, year)
    #print(fmonth)
    #print(key)
    #see if the record exists or not
    try:
        q = AWS_files.objects.get(month=fmonth)
    except:
        q = AWS_files(month=fmonth)
    #see if key exists, delete and add if it does.
    if q.key != key:
        d = AWS.objects.filter(key=q.key)
        d.delete()
        lines = importaws2.process_file(key)
        next(lines)
        for line in lines:
            #modify Data
            #print(line)
            bil_per_srt = importaws2.create_date(line[6])
            bil_per_end = importaws2.create_date(line[7])
            use_srt = importaws2.create_date(line[10])
            use_end = importaws2.create_date(line[11])
            norm_fac = importaws2.flo(line[18])
            norm_use = importaws2.flo(line[19])
            use_amt = importaws2.flo(line[17])
            unbl = importaws2.flo(line[21])
            unbc = importaws2.flo(line[22])
            br = importaws2.flo(line[23])
            bc = importaws2.flo(line[24])
            odc = importaws2.flo(line[77])
            vpcu = importaws2.flo(line[71])
            odr = importaws2.flo(line[78])
            trn = importaws2.flo(line[85])
            tru = importaws2.flo(line[86])
            upr = importaws2.flo(line[87])
            #write data
            l = AWS(identity_lineitemid= line[0],
            key = key,
            identity_timeinterval= line[1],
            bill_invoiceid= line[2],
            bill_billingentity= line[3],
            bill_billtype= line[4],
            bill_payeraccountid= line[5],
            bill_billingperiodstartdate= bil_per_srt,
            bill_billingperiodenddate= bil_per_end,
            lineitem_usageaccountid= line[8],
            lineitem_lineitemtype= line[9],
            lineitem_usagestartdate= use_srt,
            lineitem_usageenddate= use_end,
            lineitem_productcode= line[12],
            lineitem_usagetype= line[13],
            lineitem_operation= line[14],
            lineitem_availabilityzone= line[15],
            lineitem_resourceid= line[16],
            lineitem_usageamount= use_amt,
            lineitem_normalizationfactor= norm_fac,
            lineitem_normalizedusageamount= norm_use,
            lineitem_currencycode= line[20],
            lineitem_unblendedrate= unbl,
            lineitem_unblendedcost= unbc,
            lineitem_blendedrate= br,
            lineitem_blendedcost= bc,
            lineitem_lineitemdescription= line[25],
            lineitem_taxtype= line[26],
            product_productname= line[27],
            product_availability= line[28],
            product_clockspeed= line[29],
            product_currentgeneration= line[30],
            product_dedicatedebsthroughput= line[31],
            product_directorysize= line[32],
            product_directorytype= line[33],
            product_directorytypedescription= line[34],
            product_durability= line[35],
            product_ebsoptimized= line[36],
            product_endpointtype= line[37],
            product_enhancednetworkingsupported= line[38],
            product_fromlocation= line[39],
            product_fromlocationtype= line[40],
            product_group= line[41],
            product_groupdescription= line[42],
            product_instancefamily= line[43],
            product_instancetype= line[44],
            product_licensemodel= line[45],
            product_location= line[46],
            product_locationtype= line[47],
            product_maxiopsburstperformance= line[48],
            product_maxiopsvolume= line[49],
            product_maxthroughputvolume= line[50],
            product_maxvolumesize= line[51],
            product_memory= line[52],
            product_networkperformance= line[53],
            product_operatingsystem= line[54],
            product_operation= line[55],
            product_physicalprocessor= line[56],
            product_preinstalledsw= line[57],
            product_processorarchitecture= line[58],
            product_processorfeatures= line[59],
            product_productfamily= line[60],
            product_servicecode= line[61],
            product_sku= line[62],
            product_storage= line[63],
            product_storageclass= line[64],
            product_storagemedia= line[65],
            product_tenancy= line[66],
            product_tolocation= line[67],
            product_tolocationtype= line[68],
            product_transfertype= line[69],
            product_usagetype= line[70],
            product_vcpu= vpcu,
            product_version= line[72],
            product_volumetype= line[73],
            pricing_leasecontractlength= line[74],
            pricing_offeringclass= line[75],
            pricing_purchaseoption= line[76],
            pricing_publicondemandcost= odc,
            pricing_publicondemandrate= odr,
            pricing_term= line[79],
            pricing_unit= line[80],
            reservation_availabilityzone= line[81],
            reservation_normalizedunitsperreservation= line[82],
            reservation_numberofreservations= line[83],
            reservation_reservationarn= line[84],
            reservation_totalreservednormalizedunits= trn,
            reservation_totalreservedunits= tru,
            reservation_unitsperreservation= upr,
            resourcetags_aws_cloudformation_logical_id= line[88],
            resourcetags_aws_cloudformation_stack_id= line[89],
            resourcetags_aws_cloudformation_stack_name= line[90],
            resourcetags_aws_createdby= line[91],
            resourcetags_user_environment= line[92],
            resourcetags_user_graylog= line[93],
            resourcetags_user_name= line[94],
            resourcetags_user_owner= line[95],
            resourcetags_user_team= line[96])
            #save data
            l.save()
        q.key = key
        q.save()
        status = 'uploaded'
    elif q.key == key:
        status = 'latest file already uploaded'
    else:
        status = "there has been a fatal mistake"
    if int(day) < 11:
        lmonth = str(int(month)-1)
        if lmonth == '0':
            lmonth = '12'
        if int(lmonth) < 11:
            lmonth = '0'+str(lmonth)
        key = importaws2.find_key(lmonth, year)
        fmonth = importaws2.month(lmonth, year)
        try:
            q = AWS_files.objects.get(month=fmonth)
        except:
            q = AWS_files(month=fmonth)
        if q.key != key:
            d = AWS.objects.filter(key=q.key)
            d.delete()
            lines = importaws2.process_file(key)
            next(lines)
            for line in lines:
                #modify Data
                bil_per_srt = create_date(line[6])
                bil_per_end = create_date(line[7])
                use_srt = create_date(line[10])
                use_end = create_date(line[11])
                norm_fac = flo(line[18])
                norm_use = flo(line[19])
                use_amt = flo(line[17])
                unbl = flo(line[21])
                unbc = flo(line[22])
                br = flo(line[23])
                bc = flo(line[24])
                odc = flo(line[77])
                vpcu = flo(line[71])
                odr = flo(line[78])
                trn = flo(line[85])
                tru = flo(line[86])
                upr = flo(line[87])
                #write data
                l = AWS(identity_lineitemid= line[0],
                key = key,
                identity_timeinterval= line[1],
                bill_invoiceid= line[2],
                bill_billingentity= line[3],
                bill_billtype= line[4],
                bill_payeraccountid= line[5],
                bill_billingperiodstartdate= bil_per_srt,
                bill_billingperiodenddate= bil_per_end,
                lineitem_usageaccountid= line[8],
                lineitem_lineitemtype= line[9],
                lineitem_usagestartdate= use_srt,
                lineitem_usageenddate= use_end,
                lineitem_productcode= line[12],
                lineitem_usagetype= line[13],
                lineitem_operation= line[14],
                lineitem_availabilityzone= line[15],
                lineitem_resourceid= line[16],
                lineitem_usageamount= use_amt,
                lineitem_normalizationfactor= norm_fac,
                lineitem_normalizedusageamount= norm_use,
                lineitem_currencycode= line[20],
                lineitem_unblendedrate= unbl,
                lineitem_unblendedcost= unbc,
                lineitem_blendedrate= br,
                lineitem_blendedcost= bc,
                lineitem_lineitemdescription= line[25],
                lineitem_taxtype= line[26],
                product_productname= line[27],
                product_availability= line[28],
                product_clockspeed= line[29],
                product_currentgeneration= line[30],
                product_dedicatedebsthroughput= line[31],
                product_directorysize= line[32],
                product_directorytype= line[33],
                product_directorytypedescription= line[34],
                product_durability= line[35],
                product_ebsoptimized= line[36],
                product_endpointtype= line[37],
                product_enhancednetworkingsupported= line[38],
                product_fromlocation= line[39],
                product_fromlocationtype= line[40],
                product_group= line[41],
                product_groupdescription= line[42],
                product_instancefamily= line[43],
                product_instancetype= line[44],
                product_licensemodel= line[45],
                product_location= line[46],
                product_locationtype= line[47],
                product_maxiopsburstperformance= line[48],
                product_maxiopsvolume= line[49],
                product_maxthroughputvolume= line[50],
                product_maxvolumesize= line[51],
                product_memory= line[52],
                product_networkperformance= line[53],
                product_operatingsystem= line[54],
                product_operation= line[55],
                product_physicalprocessor= line[56],
                product_preinstalledsw= line[57],
                product_processorarchitecture= line[58],
                product_processorfeatures= line[59],
                product_productfamily= line[60],
                product_servicecode= line[61],
                product_sku= line[62],
                product_storage= line[63],
                product_storageclass= line[64],
                product_storagemedia= line[65],
                product_tenancy= line[66],
                product_tolocation= line[67],
                product_tolocationtype= line[68],
                product_transfertype= line[69],
                product_usagetype= line[70],
                product_vcpu= vpcu,
                product_version= line[72],
                product_volumetype= line[73],
                pricing_leasecontractlength= line[74],
                pricing_offeringclass= line[75],
                pricing_purchaseoption= line[76],
                pricing_publicondemandcost= odc,
                pricing_publicondemandrate= odr,
                pricing_term= line[79],
                pricing_unit= line[80],
                reservation_availabilityzone= line[81],
                reservation_normalizedunitsperreservation= line[82],
                reservation_numberofreservations= line[83],
                reservation_reservationarn= line[84],
                reservation_totalreservednormalizedunits= trn,
                reservation_totalreservedunits= tru,
                reservation_unitsperreservation= upr,
                resourcetags_aws_cloudformation_logical_id= line[88],
                resourcetags_aws_cloudformation_stack_id= line[89],
                resourcetags_aws_cloudformation_stack_name= line[90],
                resourcetags_aws_createdby= line[91],
                resourcetags_user_environment= line[92],
                resourcetags_user_graylog= line[93],
                resourcetags_user_name= line[94],
                resourcetags_user_owner= line[95],
                resourcetags_user_team= line[96],)
                #save data
                l.save()
            q.key = key
            q.save()
            lmstatus = 'uploaded'
        elif q.key == key:
            lmstatus = 'latest file already uploaded'
        else:
            lmstatus = 'there has been a fatal mistake'
    context = {}
    return render(request, 'warehouse/index.html', context)

def budget(request):
    def pull_budget(name):
        client = boto3.client("sts", aws_access_key_id=acc_keys.acc(), aws_secret_access_key=acc_keys.sec())
        account_id = client.get_caller_identity()["Account"]
        client = boto3.client('budgets', aws_access_key_id=acc_keys.acc(), aws_secret_access_key=acc_keys.sec())
        response = client.describe_budget(
            AccountId=str(account_id),
            BudgetName=str(name)
        )
        return response

    d = date_lib.today()
    try:
        q = AWS_Budget.objects.get(date=d)
    except:
        budget = pull_budget('Yearly Boston')
        budget = budget['Budget']
        budgetl = budget['BudgetLimit']
        limit = budgetl['Amount']
        name = budget['BudgetName']
        budgetc = budget['CalculatedSpend']
        acctD = budgetc['ActualSpend']
        acct = acctD['Amount']
        forD = budgetc['ForecastedSpend']
        forc = forD['Amount']
        acct = round(float(acct),2)
        forc = round(float(forc),2)
        q = AWS_Budget(budget_name=name, actual_spend=acct, forcasted_spend=forc, limit=limit, date=d)
        q.save()
    context = {'name':q.budget_name, 'limit':q.limit, 'actual':q.actual_spend, 'forc':q.forcasted_spend}
    return render(request, 'warehouse/budget.html', context)

def domains_update(request):
    dlist = Domain.objects.all()
    for d in dlist:
        w = whois.whois(d.name)
        d.comp = w.org
        if w.org == 'None':
            d.comp = w.registrant_org
        date_temp = w.expiration_date
        #datetemp1 = datetime.strptime(date_temp, '%Y-%m-%d %H:%M:%S')
        d.exp = date_temp
        #d.exp = None
        d.reg = w.registrar
        try:
            Resolver = dns.resolver.Resolver()
            data = Resolver.query(d.name, "NS")
            nsv = []
            for c in data:
                nsv.append(str(c))
            d.nameserver = nsv
        except:
            d.nameserver = "Not Available"
        d.save()

    return HttpResponseRedirect(reverse('w:domains'))

def domains(request):
    if request.method == 'POST':
            form = AddDomainForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                d = data['domain']
                q = Domain(name=d)
                q.save()
            return HttpResponseRedirect(reverse('w:domains'))
    else:
        form = AddDomainForm()
    dlist = Domain.objects.all().order_by('name')
    context = {'dlist': dlist, 'form': form}
    return render(request, 'warehouse/domains.html', context)

def del_domain(request, d_id):
    q = Domain.objects.get(id=d_id)
    q.delete()

    return HttpResponseRedirect(reverse('w:domains'))
