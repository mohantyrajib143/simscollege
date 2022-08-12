from website.models import slider
from django import forms

class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = '__all__'