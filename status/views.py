from django.shortcuts import render

# Create your views here.

def status_home(request):
    return render(request, "status/status_home.html" )
