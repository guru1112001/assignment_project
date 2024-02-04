from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('name', 'email', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})  # Ensure the widget type is 'date'
        }
