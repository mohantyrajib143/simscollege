from website.models import slider, about, leader, awards, student_testmonials
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

class StdTestimonialForm(forms.ModelForm):
    class Meta:
        model = student_testmonials
        fields = '__all__'