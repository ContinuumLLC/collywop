"""collywop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'importaws/(?P<tog>\d+)/$', views.importaws, name='importaws'),
    url(r'boom/$', views.boom, name='boom'),
    url(r'del_cur_month/$', views.del_cur_month, name='del_cur_month'),
    url(r'budget/$', views.budget, name='budget'),
    url(r'domains/$', views.domains, name='domains'),
    url(r'domains_update/$', views.domains_update, name='domains_update'),
    url(r'del_domain/(?P<d_id>\d+)/$', views.del_domain, name='del_domain'),
    url(r'load_files/$', views.load_files, name='load_files'),
]
