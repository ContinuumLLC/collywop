from django.db import models

# Create your models here.

class Status(models.Model):
    environment = models.TextField()
    severity = models.IntegerField()
    description = models.TextField()
    outage_start = models.DateTimeField()
    outage_detected = models.DateTimeField()
    outage_ended = models.DateTimeField()
    timezone = models.CharField(null=True, max_length=3)
    what_affected = models.TextField()
    who_affected = models.TextField()
    it_owner = models.TextField()
    rca = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.description + " " + str(self.outage_start)
