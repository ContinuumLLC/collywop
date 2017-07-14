from django.db import models
import datetime
from django.utils import timezone

# Create your models here.



class Log(models.Model):
    s_id = models.TextField()
    s_table = models.TextField()
    log_type = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return str(self.s_id)
