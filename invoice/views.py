from django.shortcuts import render

# Create your views here.
def invoice_home(request):
    return render(request, 'invoice/invoice_home.html')

def invoice_detail(request):
    return render(request, 'invoice/invoice_detail.html')
