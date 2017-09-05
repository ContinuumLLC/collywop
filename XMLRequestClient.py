import urllib.request
from xml.dom.minidom import parse

ENDPOINT_URL = "https://api.intacct.com/ia/xml/xmlgw.phtml"
TIMEOUT = 30

class XMLRequestClient:

    def __init__(self):
        pass

    @staticmethod
    def post(request):
        # Set up the url Request class and use this Content Type
        # to avoid urlencoding everything
        header = {'Content-type': 'application/xml'}
        conn = urllib.request.Request(ENDPOINT_URL, headers = header, method='POST')

        # Post the request
        result = urllib.request.urlopen(conn, request.toxml(encoding="ascii"), TIMEOUT)

        # Check the HTTP code is 200-OK
        if result.getcode() != 200:
            # Log some of the info for debugging
            raise Exception("Received HTTP status code, " + result.getcode())

        # Load the XML into the response
        response = parse(result)
        return response
