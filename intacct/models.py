from django.db import models

# Create your models here.

class Session(models.Model):
    sessionid = models.CharField(max_length=32)
    session_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.session_time)
