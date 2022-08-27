from website.models import slider, about, leader, awards, student_testmonials, alumni_testmonials, faculties, infrastructure, results, news, notice, careers, sims

from dashboard.models import tbl_rc_stream, tbl_rc_students, tbl_sc_stream
from django import forms

class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = about
        fields = '__all__'

class SimsForm(forms.ModelForm):
    class Meta:
        model = sims
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

class AlumniTestimonialForm(forms.ModelForm):
    class Meta:
        model = alumni_testmonials
        fields = '__all__'

class ChseFacultyForm(forms.ModelForm):
    class Meta:
        model = faculties
        fields = '__all__'

class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = infrastructure
        fields = '__all__'

class ResultsForm(forms.ModelForm):
    class Meta:
        model = results
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = notice
        fields = '__all__'

class CareersForm(forms.ModelForm):
    class Meta:
        model = careers
        fields = '__all__'

class RcStreamForm(forms.ModelForm):
    class Meta:
        model = tbl_rc_stream
        fields = '__all__'

class RcStudentForm(forms.ModelForm):
    class Meta:
        model = tbl_rc_students
        fields = ('regd_no', 'roll_no', 'name', 'email', 'mobile', 'gender', 'dob', 'aadhaar', 'session', 'stream', 'doj', 'father_name', 'father_occupation', 'father_mobile', 'mother_name', 'mother_occupation', 'mother_mobile', 'guardian_name', 'guardian_relation', 'guardian_mobile', 'board', 'school_name', 'school_marks', 'school_info', 'present_address', 'permanent_address', 'aadhaar_card', 'std_photo', 'std_document', 'status')
    def __init__(self, *args, **kwargs):
        super(RcStudentForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['mobile'].required = False
        self.fields['mother_mobile'].required = False
        self.fields['guardian_mobile'].required = False

class ScStreamForm(forms.ModelForm):
    class Meta:
        model = tbl_sc_stream
        fields = '__all__'