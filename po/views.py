from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import PO, Line_PO
from vendor.models import Supplier, Publisher
from .forms import POForm

def po_home(request):
    pos = PO.objects.order_by('-viewed')
    pos = pos[:10]
    context = {'pos': pos}
    return render(request, 'po/po_home.html', context)

def po_detail(request, po_id):
    pos = PO.objects.get(id=po_id)
    lines = Line_PO.objects.filter(po=pos)
    context = {'pos': pos, 'lines':lines}
    return render(request, 'po/po_detail.html', context)

def add_po(request):
    pos = PO.objects.all().order_by('-num')
    try:
        last_po = pos[0]
        next_po = int(last_po.num) + 1
    except:
        next_po = 1
    if request.method == "POST":
        form = POForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            po = PO(
                #form fields
                supplier=data['supplier'], blanket=data['blanket'], auth=data['auth'], status=data['status'], comments=data['comments'], tax=data['tax'], tax_amt=data['tax_amt'], quote=data['quote'], budgeted=data['budgeted'],
                #auto fields
                num = next_po)
            po.save()
            return HttpResponseRedirect(reverse('po:po_home'))
    else:
        form = POForm()
    context = {'form': form, 'mode': 'add'}
    return render(request, 'po/poform.html', context)

def edit_po():
    if request.method == "POST":
        form = VendorForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            v = Supplier.objects.get(id=v_id)
            v.name=data['name']
            v.portal=data['portal']
            v.desc=data['desc']
            v.modified = timezone.now()
            v.save()
            return HttpResponseRedirect(reverse('po:po_home'))
    else:
        v = Supplier.objects.get(id=v_id)
        form = VendorForm(initial = {'name': v.name, 'portal': v.portal, 'desc': v.desc})
    context = {'form': form, 'mode': 'edit', 'v_id': v_id}
    return render(request, 'po/poform.html', context)
