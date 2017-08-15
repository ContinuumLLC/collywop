from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'scrape/$', views.scraper, name='scraper'),
    url(r'^$', views.status_home, name='status_home'),
]
