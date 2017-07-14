from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

from vendor.models import Supplier, Publisher
from po.models import PO, Cost_Center

class Invoice(models.Model):
    number = models.TextField()
    supplier = models.ForeignKey(Supplier)
    po = models.ForeignKey(PO, models.SET_NULL, blank=True, null=True)
    order_num = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    tax = models.BooleanField()
    tax_amt = models.DecimalField(max_digits=5, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    cost_center = models.ForeignKey(Cost_Center, models.SET_NULL, null=True, blank=True)
    budgeted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.number)+" "+str(self.supplier.name)

class Invoice_line(models.Model):
    invoice = models.ForeignKey(Invoice)
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
    line_total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return str(self.desc)
