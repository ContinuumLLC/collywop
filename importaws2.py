import boto3, os, sys, json, csv, gzip, datetime, re
import acc_keys
from datetime import date as date_lib

path = sys.path[0]

s3 = boto3.resource('s3', aws_access_key_id=acc_keys.acc(), aws_secret_access_key=acc_keys.sec())
bucket = s3.Bucket('continuum-billing-reports-bucket')

#reggie exes
key_re = re.compile(r'(\d*-\d*)/(\w*-\w*-\w*-\w*-\w*)/DayReport-1.csv')
date_re = re.compile(r'(\d*)-(\d*)-(\d*)')

#create datetime objects
def create_date(obj):
    t = date_re.search(obj)
    if t != None:
        yr = int(t.group(1))
        mo = int(t.group(2))
        dy = int(t.group(3))
        return datetime.datetime(yr, mo, dy)
    else:
        e = 'Error'
        return e

#float or zero
def flo(obj):
    try:
        b = float(obj)
    except:
        b = 0
    return b

#needs strings that corespond to the s3 naming system
def month(m, y):
    if len(str(m))==2 and len(str(y))==4 and int(m)<13:
        if str(m) == '12':
            return str(y)+str(m)+'01-'+str(int(y)+1)+'0101'
        if int(m) <= 8:
            return str(y)+str(m)+'01-'+str(y)+'0'+str(int(m)+1)+'01'
        if int(m) >= 9:
            return str(y)+str(m)+'01-'+str(y)+str(int(m)+1)+'01'
    else:
        return "Invalid Date"

#finds the most recent file based on the manifest
def find_key(m, y):
    mon = month(m, y)
    man = bucket.Object('Hrep/DayReport/'+mon+'/DayReport-Manifest.json')
    try:
        man_content = man.get()['Body'].read().decode('utf-8')
        man_json = json.loads(man_content)
        key = man_json['reportKeys']
        return key[0]
    except:
        return "No data or imput error"

#process csv file
def process_file(key):
    data = bucket.Object(key)
    gdata = data.get()['Body']
    csvf = gzip.open(gdata, mode="rt")
    lines = csv.reader(csvf, 'excel')
    return lines
