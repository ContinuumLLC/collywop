from django.shortcuts import render

# Create your views here.
from .models import PO, Line_PO
from vendor.models import Supplier, Publisher

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
