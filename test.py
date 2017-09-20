import acc_keys
from xml.dom.minidom import Document
from XMLRequestClient import XMLRequestClient
import time
from xml.dom.minidom import parse

def create_session():
    try:
        # Write the XML request with the minidom  module
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
        print('1')
        operation = newdoc.createElement('operation')
        request.appendChild(operation)
        print('2')
        authentication = newdoc.createElement('authentication')
        operation.appendChild(operation)
        print('3')
        ses = 'test'

        sessionid = newdoc.createElement('sessionid')
        authentication.appendChild(sessionid).appendChild(newdoc.createTextNode(ses))
        print('4')
        content = newdoc.createElement('content')
        operation.appendChild(content)
        print('5')
        function = newdoc.createElement('function')
        content.appendChild(function).setAttributeNode(newdoc.createAttribute('controlid'))
        function.attributes["controlid"].value = "1"
        print('6')
        read = newdoc.createElement('readByQuery')
        function.appendChild(read)
        print('7')
        objectt = newdoc.createElement('object')
        read.appendChild(objectt).appendChild(newdoc.createTextNode('VENDOR'))
        print('8')
        fields = newdoc.createElement('fields')
        read.appendChild(objectt).appendChild(newdoc.createTextNode('*'))
        print('9')
        query = newdoc.createElement('query')
        read.appendChild(query)
        print('10')
        pagesize = newdoc.createElement('pagesize')
        read.appendChild(pagesize).appendChild(newdoc.createTextNode('3'))

        print(request.toprettyxml())

        # Print the XML response to the console
        #print(result.toprettyxml())

        find = result.getElementsByTagName('sessionid')
        sessionid = find[0].firstChild.nodeValue
        return sessionid

    except Exception as inst:
        print("Uh oh, something is wrong")
        print(type(inst))
        print(inst.args)

create_session()
