from website.models import slider, about, leader
from django import forms

class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = about
        fields = '__all__'

class LeaderForm(forms.ModelForm):
    class Meta:
        model = leader
        fields = '__all__'