from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone_number', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
