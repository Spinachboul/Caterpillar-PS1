from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = '__all__'  # Use '__all__' to include all fields in the form
