from django import forms
from .models import Property,Unit,Tenant,Vendor,Lease,Payment,Expense

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["propertyName","address","city","county"]

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["firstName","lastName"]