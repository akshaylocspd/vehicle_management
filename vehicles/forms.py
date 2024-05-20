from django import forms
from .models import Vehicle, Chalan

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'registration_number', 'model', 'make', 'color', 
            'owner_name', 'address', 'mobile_number', 'email'
        ]

class ChalanForm(forms.ModelForm):
    class Meta:
        model = Chalan
        fields = ['vehicle', 'amount', 'description', 'location', 'vehicle_class', 'violator_type', 'offence_committed']
