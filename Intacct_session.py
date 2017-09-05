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

        operation = newdoc.createElement('operation')
        request.appendChild(operation)

        authentication = newdoc.createElement('authentication')
        operation.appendChild(authentication)

        login = newdoc.createElement('login')
        authentication.appendChild(login)

        userid = newdoc.createElement('userid')
        login.appendChild(userid).appendChild(newdoc.createTextNode(acc_keys.int_user()))

        companyid = newdoc.createElement('companyid')
        login.appendChild(companyid).appendChild(newdoc.createTextNode(acc_keys.int_company_id()))

        password = newdoc.createElement('password')
        login.appendChild(password).appendChild(newdoc.createTextNode(acc_keys.int_user_pass()))

        content = newdoc.createElement('content')
        operation.appendChild(content)

        function = newdoc.createElement('function')
        content.appendChild(function).setAttributeNode(newdoc.createAttribute('controlid'))
        function.attributes["controlid"].value = "1"

        create = newdoc.createElement('getAPISession')
        function.appendChild(create)


        #print(request.toprettyxml())

        # Post the request
        result = XMLRequestClient.post(request)

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
