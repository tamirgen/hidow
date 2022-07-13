from django import forms
from .models import WarrantyRegistration

class WarrantyForm(forms.ModelForm):

    model = WarrantyRegistration
    fields = ("product", "full_name", "email", "street_address1",
                "street_address2", "postcode", "town_or_city",
                "country", "date")
