from website.models import slider, about, leader, awards
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

class AwardForm(forms.ModelForm):
    class Meta:
        model = awards
        fields = '__all__'