from django import forms
from .models import UserAddress

# useraddress form
class UserAddressForm(forms.ModelForm):
    default = forms.BooleanField(label='Make Default')
    class Meta:
        model = UserAddress
        fields = [
            "address",
            "address2",
            "city",
            "state",
            "country",
            "postalcode",
            "phone",
            "billing"
        ]
