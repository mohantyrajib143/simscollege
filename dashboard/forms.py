from website.models import slider, about
from django import forms

class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = about
        fields = '__all__'