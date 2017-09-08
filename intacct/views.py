from django.shortcuts import render

# Create your views here.

from XMLRequestClient import XMLRequestClient
import Intacct_session
import acc_keys
from xml.dom.minidom import Document
import time
from xml.dom.minidom import parse

from .models import Session

def update_session(request):
    #get session id
    sessionid = Intacct_session.create_session()
    s = Session(sessionid=sessionid)
    s.save()
    context = {'sessionid': sessionid}

    return render(request, 'intacct/session.html', context)

def vendors(request):

    vens = []

    #pull vendors, filter by entity
    newdoc = Document();
    request = newdoc.createElement('request')
    newdoc.appendChild(request)
    control = newdoc.createElement('control')
    request.appendChild(control)
    senderid = newdoc.createElement('senderid')
    control.appendChild(senderid).appendChild(newdoc.createTextNode(acc_keys.int_sender_id()))
    senderpassword = newdoc.createElement('password')
    control.appendChild(senderpassword).appendChild(newdoc.createTextNode(acc_keys.int_sender_pass()))
    controlid = newdoc.createElement('controlid')
    control.appendChild(controlid).appendChild(newdoc.createTextNode(str(int(time.time()))))
    uniqueid = newdoc.createElement('uniqueid')
    control.appendChild(uniqueid).appendChild(newdoc.createTextNode("false"))
    dtdversion = newdoc.createElement('dtdversion')
    control.appendChild(dtdversion).appendChild(newdoc.createTextNode("3.0"))
    includewhitespace = newdoc.createElement('includewhitespace')
    control.appendChild(includewhitespace).appendChild(newdoc.createTextNode("false"))

    operation = newdoc.createElement('operation')
    request.appendChild(operation)

    authentication = newdoc.createElement('authentication')
    operation.appendChild(operation)

    s = Session.objects.order_by('-session_time')
    ses = s[0].sessionid

    sessionid = newdoc.createElement('sessionid')
    authentication.appendChild(authentication).appendChild(newdoc.createTextNode(ses))

    content = newdoc.createElement('content')
    operation.appendChild(content)

    function = newdoc.createElement('function')
    content.appendChild(function).setAttributeNode(newdoc.createAttribute('controlid'))
    function.attributes["controlid"].value = "1"

    read = newdoc.createElement('readByQuery')
    function.appendChild(read)

    objectt = newdoc.createElement('object')
    read.appendChild(objectt).appendChild(newdoc.createTextNode('VENDOR'))

    fields = newdoc.createElement('fields')
    read.appendChild(objectt).appendChild(newdoc.createTextNode('*'))

    query = newdoc.createElement('query')
    read.appendChild(query)

    pagesize = newdoc.createElement('pagesize')
    read.appendChild(pagesize).appendChild(newdoc.createTextNode('3'))

    print(request.toprettyxml())
    #print(request)
    # Post the request
    result = XMLRequestClient.post(request)

    for vendor in result.getElementsByTagName('vendor'):
        for tag in vendor.getElementsByTagName('DISPLAYCONTACT.PRINTAS'):
            ven = tag[0].firstChild.nodeValue
            vens.append(ven)


    #paginate
    #finish pagination
    #send list
    context = {vens}
    return render(request, 'intacct/vendors.html', context)
