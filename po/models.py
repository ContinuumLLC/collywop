from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

from vendor.models import Supplier, Publisher
from quote.models import Quote

class Cost_Center(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User)

class PO(models.Model):
    supplier = models.ForeignKey(Supplier)
    num = models.IntegerField()
    issued = models.DateTimeField(null=True, blank=True)
    blanket = models.BooleanField()
    auth = models.ForeignKey(User)
    status = models.TextField() #make this a dropdown?
    comments = models.TextField(null=True, blank=True)
    #add tax handling
    tax = models.BooleanField()
    tax_amt = models.DecimalField(max_digits=5, decimal_places=5)
    subtotal = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    quote = models.ForeignKey(Quote, models.SET_NULL, null=True, blank=True)
    cost_center = models.ForeignKey(Cost_Center, models.SET_NULL, null=True, blank=True)
    budgeted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.supplier.name)+str(self.num)

class Line_PO(models.Model):
    po = models.ForeignKey(PO)
    desc = models.TextField()
    item_num = models.TextField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, models.SET_NULL, null=True, blank=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=10)
    uom = models.TextField()
    unit_cost = models.DecimalField(max_digits=19, decimal_places=10)
    dept_code = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    line_total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    def __str__(self):
        return str(self.desc)
