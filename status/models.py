from django.db import models

# Create your models here.

class Status(models.Model):
    environment = models.TextField()
    severity = models.IntegerField()
    description = models.TextField(null=True)
    outage_start = models.DateTimeField()
    outage_detected = models.DateTimeField()
    outage_ended = models.DateTimeField()
    timezone = models.CharField(null=True, max_length=3)
    what_affected = models.TextField()
    who_affected = models.TextField(null=True)
    it_owner = models.TextField(null=True)
    rca = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.description + " " + str(self.outage_start)

class Site(models.Model):
    name = models.TextField()
    url = models.URLField()
    def __str__(self):
        return self.name

class Availability(models.Model):
    site = models.ForeignKey(Site)
    status = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
