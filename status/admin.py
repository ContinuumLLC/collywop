from django.contrib import admin

# Register your models here.

from .models import Status, Site, Availability

admin.site.register(Status)
admin.site.register(Site)
admin.site.register(Availability)
