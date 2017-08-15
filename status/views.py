from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests

# Create your views here.

from .models import Status, Site, Availability

def status_home(request):
    site_status = {}
    sites = Site.objects.all()
    avs = Availability.objects.all()
    for site in sites:
        av = avs.filter(site=site).order_by('-time')
        s = av[0]
        site_status[site] = s.status
    context = {'site_status': site_status}
    return render(request, "status/status_home.html", context)

def simple_checker(site):
    try:
        req = requests.get(site)
        if req.status_code == requests.codes.ok:
            s = 1
        else:
            s = 0
    except:
        s = 0
    return s

def scraper(request):
    sites = Site.objects.all()
    for site in sites:
        s = simple_checker(site.url)
        r = Availability(site=site, status=s)
        r.save()
    return HttpResponseRedirect(reverse('status:status_home'))
