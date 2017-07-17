from django import forms

from .models import PO, Line_PO, Cost_Center
from vendor.models import Supplier, Publisher
from quote.models import Quote
from django.contrib.auth.models import User


class POForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    blanket = forms.BooleanField(required=False)
    auth = forms.ModelChoiceField(queryset=User.objects.all())
    status = forms.CharField(strip=True) #make this a dropdown?
    comments = forms.CharField(strip=True, required=False)
    #add tax handling
    tax = forms.BooleanField(required=False)
    tax_amt = forms.DecimalField(max_digits=5, decimal_places=5, required=False)
    quote = forms.ModelChoiceField(queryset=Quote.objects.all(), required=False)
    budgeted = forms.BooleanField()


class CostCenterForm(forms.Form):
    pass


#cost_center = forms.ModelChoiceField(queryset=Cost_Center.objects.all())
