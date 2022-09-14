from asyncio import streams
from operator import concat
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from website.models import slider, about, leader, awards, student_testmonials, alumni_testmonials, faculties, infrastructure, results, news, notice, careers, JobApply, sims, contact
from django.contrib import messages
from . forms import SliderForm, AboutForm, LeaderForm, AwardForm, StdTestimonialForm, AlumniTestimonialForm, ChseFacultyForm, InfrastructureForm, ResultsForm, NewsForm, NoticeForm, CareersForm, SimsForm, RcStreamForm, RcStudentForm, ScStreamForm, ScStudentForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from urllib import request
from django.contrib.auth.models import User
from dashboard.models import password_token, tbl_rc_std_payments, tbl_rc_stream, tbl_rc_students, tbl_sc_stream, tbl_sc_students, tbl_sc_std_payments
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from college.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.db.models import Count
from num2words import num2words
import random
from django.db.models import Sum

# Create your views here.
def mylogin(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, 'Successfully Login!')
			else:
				messages.error(request, 'Username and password is not correct, Please try again!')
		return render(request, 'dashboard/login.html')

def mylogout(request):
	logout(request)
	return redirect('mylogin')

import uuid
def forgot_pass(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not User.objects.filter(email=email).first():
                messages.error(request, 'No user found with this email, plz try another email')
                return redirect('forgot_pass')
            else :
                myemail = request.POST.get('email')
                user_obj = User.objects.get(email = myemail)
                fname = user_obj.first_name
                token = str(uuid.uuid4())
                password_obj= password_token.objects.get(user = user_obj)
                password_obj.forget_password_token = token
                password_obj.save()

                # sending email starts
                html_content = render_to_string("dashboard/forgot_pass_email.html",{'title':'Forgot Password','token':token, 'fname':fname})
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    "Forgot password request at SIMS",
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [myemail]
                )
                email.attach_alternative(html_content,"text/html")
                email.send()

                messages.success(request, 'An email with reset password link is sent.')
                return redirect('forgot_pass')   
    except Exception as e:
        print(e)
    return render(request,'dashboard/forgot_pass.html')

def reset_password(request, token):
    data = {}
    try:
        password_obj = password_token.objects.filter(forget_password_token = token).first()
        data = {'user_id' : password_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_pass')
            confirm_password = request.POST.get('cnf_pass')
            user_id = request.POST.get('user_id')
            
            if new_password != confirm_password:
                messages.error(request, 'Password and Confirm password both should  be equal.')
                return redirect(f'/dashboard/reset_password/{token}/')

            else:
                user_obj = User.objects.get(id = user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request, 'Your password changed sucessfully, try to login to admin dashboard!')
                return redirect(f'/dashboard/reset_password/{token}/')
    except Exception as e:
        print(e)
    return render(request,'dashboard/reset_pass.html', data)

@login_required(login_url='mylogin')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='mylogin')
def manage_slider(request):
    if request.method=='POST':
        title = request.POST['title']
        image = request.FILES['image']
        status = 'Active'

        data = slider(title=title, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_slider')
    else:
        allSlider = slider.objects.all().order_by('-id')
        data = {'allSlider':allSlider}
        return render(request, 'dashboard/manage_slider.html', data)

@login_required(login_url='mylogin')
def update_slider(request, id):
    update = slider.objects.get(id=id)
    if request.FILES:
        slider.objects.get(id=id).image.delete(save=True)
    query = SliderForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_slider')

@login_required(login_url='mylogin')
def update_slider_status(request, id):
    query = slider.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_slider')

@login_required(login_url='mylogin')
def delete_slider(request, id):
    db = slider.objects.get(id=id)
    file = slider.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_slider')

@login_required(login_url='mylogin')
def manage_sims(request):
    query = sims.objects.filter(id=1)
    data = {'query':query[0]}
    return render(request, 'dashboard/manage_sims.html', data)

@login_required(login_url='mylogin')
def update_sims(request):
    update = sims.objects.get(id=1)
    query = SimsForm(request.POST, instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_sims')

@login_required(login_url='mylogin')
def manage_aboutus(request):
    query = about.objects.filter(id=1)
    data = {'query':query[0]}
    return render(request, 'dashboard/manage_aboutus.html', data)

@login_required(login_url='mylogin')
def update_aboutus(request):
    update = about.objects.get(id=1)
    query = AboutForm(request.POST, instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_aboutus')

@login_required(login_url='mylogin')
def manage_leader(request):
    allLeader = leader.objects.all()
    data = {'allLeader':allLeader}
    return render(request, 'dashboard/manage_leader.html', data)

@login_required(login_url='mylogin')
def update_leader(request, id):
    update = leader.objects.get(id=id)
    if request.FILES:
        leader.objects.get(id=id).image.delete(save=True)
    query = LeaderForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_leader')

@login_required(login_url='mylogin')
def manage_awards(request):
    if request.method=='POST':
        title = request.POST['title']
        award = request.POST['award']
        image = request.FILES['image']

        data = awards(title=title, award=award, image=image)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_awards')
    else:
        allAwards = awards.objects.all().order_by('-id')
        data = {'allAwards':allAwards}
        return render(request, 'dashboard/manage_awards.html', data)

@login_required(login_url='mylogin')
def update_awards(request, id):
    update = awards.objects.get(id=id)
    if request.FILES:
        awards.objects.get(id=id).image.delete(save=True)
    query = AwardForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_awards')

@login_required(login_url='mylogin')
def delete_awards(request, id):
    db = awards.objects.get(id=id)
    file = awards.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_awards')

@login_required(login_url='mylogin')
def manage_stdtestimonial(request):
    if request.method=='POST':
        name = request.POST['name']
        position = request.POST['position']
        image = request.FILES['image']
        message = request.POST['message']
        status = 'Active'

        data = student_testmonials(name=name, position=position, image=image, message=message, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_stdtestimonial')
    else:
        stdTestimonial = student_testmonials.objects.all().order_by('-id')
        data = {'stdTestimonial':stdTestimonial}
        return render(request, 'dashboard/manage_stdtestimonial.html', data)

@login_required(login_url='mylogin')
def update_stdtestimonial(request, id):
    update = student_testmonials.objects.get(id=id)
    if request.FILES:
        student_testmonials.objects.get(id=id).image.delete(save=True)
    query = StdTestimonialForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_stdtestimonial')

@login_required(login_url='mylogin')
def update_stdtestimonial_status(request, id):
    query = student_testmonials.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_stdtestimonial')

@login_required(login_url='mylogin')
def delete_stdtestimonial(request, id):
    db = student_testmonials.objects.get(id=id)
    file = student_testmonials.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_stdtestimonial')

@login_required(login_url='mylogin')
def manage_alumni_testimonial(request):
    if request.method=='POST':
        name = request.POST['name']
        position = request.POST['position']
        image = request.FILES['image']
        message = request.POST['message']
        status = 'Active'

        data = alumni_testmonials(name=name, position=position, image=image, message=message, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_alumni_testimonial')
    else:
        alumniTestimonial = alumni_testmonials.objects.all().order_by('-id')
        data = {'alumniTestimonial':alumniTestimonial}
        return render(request, 'dashboard/manage_alumni_testimonial.html', data)

@login_required(login_url='mylogin')
def update_alumni_testimonial(request, id):
    update = alumni_testmonials.objects.get(id=id)
    if request.FILES:
        alumni_testmonials.objects.get(id=id).image.delete(save=True)
    query = AlumniTestimonialForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_alumni_testimonial')

@login_required(login_url='mylogin')
def update_alumni_testimonial_status(request, id):
    query = alumni_testmonials.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_alumni_testimonial')

@login_required(login_url='mylogin')
def delete_alumni_testimonial(request, id):
    db = alumni_testmonials.objects.get(id=id)
    file = alumni_testmonials.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_alumni_testimonial')

@login_required(login_url='mylogin')
def manage_chse_faculty(request):
    if request.method=='POST':
        type = 'CHSE'
        name = request.POST['name']
        position = request.POST['position']
        experience = request.POST['experience']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        whatsapp = request.POST['whatsapp']
        gmail = request.POST['gmail']
        image = request.FILES['image']
        status = 'Active'

        data = faculties(type=type ,name=name, position=position, experience=experience, facebook=facebook, instagram=instagram, linkedin=linkedin, whatsapp=whatsapp, gmail=gmail, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_chse_faculty')
    else:
        chseFaculty = faculties.objects.filter(type='CHSE').order_by('-id')
        data = {'chseFaculty':chseFaculty}
        return render(request, 'dashboard/manage_chse_faculty.html', data)

@login_required(login_url='mylogin')
def update_chse_faculty(request, id):
    update = faculties.objects.get(id=id)
    if request.FILES:
        faculties.objects.get(id=id).image.delete(save=True)
    query = ChseFacultyForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_chse_faculty')

@login_required(login_url='mylogin')
def update_chse_faculty_status(request, id):
    query = faculties.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_chse_faculty')

@login_required(login_url='mylogin')
def delete_chse_faculty(request, id):
    db = faculties.objects.get(id=id)
    file = faculties.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_chse_faculty')

@login_required(login_url='mylogin')
def manage_entrance_faculty(request):
    if request.method=='POST':
        type = 'ENTRANCE'
        name = request.POST['name']
        position = request.POST['position']
        experience = request.POST['experience']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        whatsapp = request.POST['whatsapp']
        gmail = request.POST['gmail']
        image = request.FILES['image']
        status = 'Active'

        data = faculties(type=type ,name=name, position=position, experience=experience, facebook=facebook, instagram=instagram, linkedin=linkedin, whatsapp=whatsapp, gmail=gmail, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_entrance_faculty')
    else:
        EntranceFaculty = faculties.objects.filter(type='ENTRANCE').order_by('-id')
        data = {'EntranceFaculty':EntranceFaculty}
        return render(request, 'dashboard/manage_entrance_faculty.html', data)

@login_required(login_url='mylogin')
def update_entrance_faculty(request, id):
    update = faculties.objects.get(id=id)
    if request.FILES:
        faculties.objects.get(id=id).image.delete(save=True)
    query = ChseFacultyForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_entrance_faculty')

@login_required(login_url='mylogin')
def update_entrance_faculty_status(request, id):
    query = faculties.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_entrance_faculty')

@login_required(login_url='mylogin')
def delete_entrance_faculty(request, id):
    db = faculties.objects.get(id=id)
    file = faculties.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_entrance_faculty')

@login_required(login_url='mylogin')
def manage_college(request):
    if request.method=='POST':
        type = 'COLLEGE'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_college')
    else:
        college = infrastructure.objects.filter(type='COLLEGE').order_by('-id')
        data = {'college':college}
        return render(request, 'dashboard/manage_college.html', data)

@login_required(login_url='mylogin')
def update_college(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_college')

@login_required(login_url='mylogin')
def update_college_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_college')

@login_required(login_url='mylogin')
def delete_college(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_college')

@login_required(login_url='mylogin')
def manage_hostel(request):
    if request.method=='POST':
        type = 'HOSTEL'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_hostel')
    else:
        hostel = infrastructure.objects.filter(type='HOSTEL').order_by('-id')
        data = {'hostel':hostel}
        return render(request, 'dashboard/manage_hostel.html', data)

@login_required(login_url='mylogin')
def update_hostel(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_hostel')

@login_required(login_url='mylogin')
def update_hostel_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_hostel')

@login_required(login_url='mylogin')
def delete_hostel(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_hostel')

@login_required(login_url='mylogin')
def manage_gallery(request):
    if request.method=='POST':
        type = 'GALLERY'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_gallery')
    else:
        gallery = infrastructure.objects.filter(type='GALLERY').order_by('-id')
        data = {'gallery':gallery}
        return render(request, 'dashboard/manage_gallery.html', data)

@login_required(login_url='mylogin')
def update_gallery(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_gallery')

@login_required(login_url='mylogin')
def update_gallery_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_gallery')

@login_required(login_url='mylogin')
def delete_gallery(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_gallery')

@login_required(login_url='mylogin')
def manage_labs(request):
    if request.method=='POST':
        type = 'LAB'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_labs')
    else:
        labs = infrastructure.objects.filter(type='LAB').order_by('-id')
        data = {'labs':labs}
        return render(request, 'dashboard/manage_labs.html', data)

@login_required(login_url='mylogin')
def update_labs(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_labs')

@login_required(login_url='mylogin')
def update_labs_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_labs')

@login_required(login_url='mylogin')
def delete_labs(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_labs')

@login_required(login_url='mylogin')
def manage_sports(request):
    if request.method=='POST':
        type = 'SPORTS'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_sports')
    else:
        sports = infrastructure.objects.filter(type='SPORTS').order_by('-id')
        data = {'sports':sports}
        return render(request, 'dashboard/manage_sports.html', data)

@login_required(login_url='mylogin')
def update_sports(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_sports')

@login_required(login_url='mylogin')
def update_sports_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_sports')

@login_required(login_url='mylogin')
def delete_sports(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_sports')

@login_required(login_url='mylogin')
def manage_yoga(request):
    if request.method=='POST':
        type = 'YOGA'
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = infrastructure(type=type, title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_yoga')
    else:
        yoga = infrastructure.objects.filter(type='YOGA').order_by('-id')
        data = {'yoga':yoga}
        return render(request, 'dashboard/manage_yoga.html', data)

@login_required(login_url='mylogin')
def update_yoga(request, id):
    update = infrastructure.objects.get(id=id)
    if request.FILES:
        infrastructure.objects.get(id=id).image.delete(save=True)
    query = InfrastructureForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_yoga')

@login_required(login_url='mylogin')
def update_yoga_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_yoga')

@login_required(login_url='mylogin')
def delete_yoga(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_yoga')

@login_required(login_url='mylogin')
def manage_neet(request):
    if request.method=='POST':
        type = 'NEET'
        name = request.POST['name']
        position = request.POST['position']
        image = request.FILES['image']
        status = 'Active'

        data = results(type=type, name=name, position=position, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_neet')
    else:
        neet = results.objects.filter(type='NEET').order_by('-id')
        data = {'neet':neet}
        return render(request, 'dashboard/manage_neet.html', data)

@login_required(login_url='mylogin')
def update_neet(request, id):
    update = results.objects.get(id=id)
    if request.FILES:
        results.objects.get(id=id).image.delete(save=True)
    query = ResultsForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_neet')

@login_required(login_url='mylogin')
def update_neet_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_neet')

@login_required(login_url='mylogin')
def delete_neet(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_neet')

@login_required(login_url='mylogin')
def manage_iit(request):
    if request.method=='POST':
        type = 'IIT'
        name = request.POST['name']
        position = request.POST['position']
        image = request.FILES['image']
        status = 'Active'

        data = results(type=type, name=name, position=position, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_iit')
    else:
        iit = results.objects.filter(type='IIT').order_by('-id')
        data = {'iit':iit}
        return render(request, 'dashboard/manage_iit.html', data)

@login_required(login_url='mylogin')
def update_iit(request, id):
    update = results.objects.get(id=id)
    if request.FILES:
        results.objects.get(id=id).image.delete(save=True)
    query = ResultsForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_iit')

@login_required(login_url='mylogin')
def update_iit_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_iit')

@login_required(login_url='mylogin')
def delete_iit(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_iit')

@login_required(login_url='mylogin')
def manage_chse(request):
    if request.method=='POST':
        type = 'CHSE'
        name = request.POST['name']
        position = request.POST['position']
        image = request.FILES['image']
        status = 'Active'

        data = results(type=type, name=name, position=position, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_chse')
    else:
        chse = results.objects.filter(type='CHSE').order_by('-id')
        data = {'chse':chse}
        return render(request, 'dashboard/manage_chse.html', data)

@login_required(login_url='mylogin')
def update_chse(request, id):
    update = results.objects.get(id=id)
    if request.FILES:
        results.objects.get(id=id).image.delete(save=True)
    query = ResultsForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_chse')

@login_required(login_url='mylogin')
def update_chse_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_chse')

@login_required(login_url='mylogin')
def delete_chse(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_chse')

@login_required(login_url='mylogin')
def manage_news(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        status = 'Active'

        data = news(title=title, description=description, image=image, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_news')
    else:
        allNews = news.objects.all().order_by('-id')
        data = {'news':allNews}
        return render(request, 'dashboard/manage_news.html', data)

@login_required(login_url='mylogin')
def update_news(request, id):
    update = news.objects.get(id=id)
    if request.FILES:
        news.objects.get(id=id).image.delete(save=True)
    query = NewsForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_news')

@login_required(login_url='mylogin')
def update_news_status(request, id):
    query = news.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_news')

@login_required(login_url='mylogin')
def delete_news(request, id):
    db = news.objects.get(id=id)
    file = news.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_news')

@login_required(login_url='mylogin')
def manage_notices(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        status = 'Active'

        data = notice(title=title, description=description, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_notices')
    else:
        allNotice = notice.objects.all().order_by('-id')
        data = {'notice':allNotice}
        return render(request, 'dashboard/manage_notices.html', data)

@login_required(login_url='mylogin')
def update_notices(request, id):
    update = notice.objects.get(id=id)
    if request.FILES:
        notice.objects.get(id=id).image.delete(save=True)
    query = NoticeForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_notices')

@login_required(login_url='mylogin')
def update_notices_status(request, id):
    query = notice.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_notices')

@login_required(login_url='mylogin')
def delete_notices(request, id):
    db = notice.objects.get(id=id)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_notices')

@login_required(login_url='mylogin')
def manage_careers(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']
        experience = request.POST['experience']
        qualification = request.POST['qualification']
        status = 'Active'

        data = careers(title=title, description=description, experience=experience, qualification=qualification, status=status)
        data.save()
        messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_careers')
    else:
        allCareers = careers.objects.all().order_by('-id')
        data = {'careers':allCareers}
        return render(request, 'dashboard/manage_careers.html', data)

@login_required(login_url='mylogin')
def update_careers(request, id):
    update = careers.objects.get(id=id)
    if request.FILES:
        careers.objects.get(id=id).image.delete(save=True)
    query = CareersForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_careers')

@login_required(login_url='mylogin')
def update_careers_status(request, id):
    query = careers.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_careers')

@login_required(login_url='mylogin')
def delete_careers(request, id):
    db = careers.objects.get(id=id)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_careers')

@login_required(login_url='mylogin')
def manage_jobapplied(request):
    job = JobApply.objects.all().order_by('-id')
    data = {'job':job}
    return render(request, 'dashboard/manage_jobapplied.html', data)

@login_required(login_url='mylogin')
def manage_conatctInfo(request):
    contactInfo = contact.objects.all().order_by('-id')
    data = {'contactInfo':contactInfo}
    return render(request, 'dashboard/manage_contactInfo.html', data)

@login_required(login_url='mylogin')
def manage_rc_stream(request):
    if request.method=='POST':
        stream = request.POST['stream']
        session = request.POST['session']
        duration = request.POST['duration']
        fees = request.POST['fees']
        status = 'Active'

        if tbl_rc_stream.objects.filter(stream=stream, session=session).exists():
            messages.error(request, 'Stream and session data can not be duplicate')
        else:
            data = tbl_rc_stream(stream=stream, session=session, duration=duration, fees=fees, status=status)
            data.save()
            messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_rc_stream')
    else:
        cyear = date.today().year
        nyear = date.today().year + 2
        rc_stream = tbl_rc_stream.objects.all().order_by('-id')
        data = {'rc_stream':rc_stream, 'cyear':cyear, 'nyear':nyear}
        return render(request, 'dashboard/manage_rc_stream.html', data)

@login_required(login_url='mylogin')
def update_rc_stream(request, id):
    update = tbl_rc_stream.objects.get(id=id)
    query = RcStreamForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_rc_stream')

@login_required(login_url='mylogin')
def update_rc_stream_status(request, id):
    query = tbl_rc_stream.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_rc_stream')

@login_required(login_url='mylogin')
def delete_rc_stream(request, id):
    db = tbl_rc_stream.objects.get(id=id)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_rc_stream')

@login_required(login_url='mylogin')
def manage_rc_student(request):
    allStd = tbl_rc_students.objects.all().order_by('-id')
    data = {'allStd':allStd, 'ttlStd':allStd.count()}
    return render(request, 'dashboard/manage_rc_student.html', data)

@login_required(login_url='mylogin')
def view_rc_student_info(request, id):
    if tbl_rc_students.objects.filter(id=id).exists():
        stdInfo = tbl_rc_students.objects.get(id=id)
        stdFees = tbl_rc_std_payments.objects.filter(std_id=id).order_by('-id')
        streamInfo = tbl_rc_stream.objects.get(stream=stdInfo.stream, session=stdInfo.session, status='Active')
        totalPaid = tbl_rc_std_payments.objects.filter(std_id=stdInfo.id).aggregate(ttlAmount=Sum('amount'))
        feesAmount = int(streamInfo.fees)
        paidAmount = int(totalPaid['ttlAmount'])
        remainingAmount = feesAmount - paidAmount
        data = {'stdInfo':stdInfo, 'stdFees':stdFees, 'feesAmount':feesAmount, 'paidAmount':paidAmount, 'remainingAmount':remainingAmount}
        return render(request, 'dashboard/view_rc_student_info.html', data)
    else:
        return render(request, 'dashboard/404.html')

@login_required(login_url='mylogin')
def update_rc_student_status(request, id):
    query = tbl_rc_students.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    return redirect('manage_rc_student')

@login_required(login_url='mylogin')
def edit_rc_student(request, id):
    if tbl_rc_students.objects.filter(id=id).exists():
        query = tbl_rc_students.objects.get(id=id)
        data = {'query':query}
        return render(request, 'dashboard/edit_rc_student.html', data)
    else:
        return render(request, 'dashboard/404.html')

@login_required(login_url='mylogin')
def update_rc_student(request, id):
    update = tbl_rc_students.objects.get(id=id)
    stdData = RcStudentForm(request.POST or None, request.FILES, instance=update)
    stdData.save()
    if stdData.is_valid():
        stdData.save(commit=True)
        messages.success(request, 'Successfully Updated!')
    return redirect('manage_rc_student')

@login_required(login_url='mylogin')
def add_rc_student(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        dob = request.POST['dob']
        aadhaar = request.POST['aadhaar']
        session = request.POST['session']
        stream = request.POST['stream']
        doj = request.POST['doj']
        father_name = request.POST['father_name']
        father_occupation = request.POST['father_occupation']
        father_mobile = request.POST['father_mobile']
        mother_name = request.POST['mother_name']
        mother_occupation = request.POST['mother_occupation']
        mother_mobile = request.POST['mother_mobile']
        guardian_name = request.POST['guardian_name']
        guardian_relation = request.POST['guardian_relation']
        guardian_mobile = request.POST['guardian_mobile']
        board = request.POST['board']
        school_name = request.POST['school_name']
        school_marks = request.POST['school_marks']
        school_info = request.POST['school_info']
        present_address = request.POST['present_address']
        permanent_address = request.POST['permanent_address']
        aadhaar_card = request.FILES['aadhaar_card']
        std_photo = request.FILES['std_photo']
        std_document = request.FILES['std_document']
        status = 'Active'

        if tbl_rc_students.objects.filter(aadhaar=aadhaar).exists():
            messages.error(request, 'Aadhaar No is exist!!')
        else:
            data = tbl_rc_students(name=name, email=email, mobile=mobile,gender=gender, dob=dob, aadhaar=aadhaar, session=session, stream=stream, doj=doj, father_name=father_name, father_occupation=father_occupation, father_mobile=father_mobile, mother_name=mother_name, mother_occupation=mother_occupation, mother_mobile=mother_mobile, guardian_name=guardian_name, guardian_relation=guardian_relation, guardian_mobile=guardian_mobile, board=board, school_name=school_name, school_marks=school_marks, school_info=school_info, present_address=present_address, permanent_address=permanent_address, aadhaar_card=aadhaar_card, std_photo=std_photo, std_document=std_document, status=status)
            data.save()

            laststdID = tbl_rc_students.objects.latest('id')
            request.session['stdID'] = laststdID.id
        return redirect('rc_student_admission_payment')
    else:
        cyear = date.today().year
        nyear = date.today().year + 2
        session = str(cyear) + "-" + str(nyear)

        data = {'session':session}
        return render(request, 'dashboard/add_rc_student.html', data)

@login_required(login_url='mylogin')
def rc_student_admission_payment(request):
    if 'stdID' in request.session:
        if request.method=='POST':
            std_id = request.POST['std_id']
            rollno = request.POST['rollno']
            regdno = request.POST['regdno']
            invoice = str(random.randint(1000000000, 9999999999))
            txn = str(random.randint(1000000000, 9999999999))
            txn_id = 'txn' + txn
            amount = request.POST['amount']
            type = request.POST['type']
            if type == 'OFFLINE':
                mode = request.POST['offline_mode']
            else:
                mode = request.POST['online_mode']
            remarks = request.POST['remarks']
            pdate = request.POST['date']
            status = 'active'

            data = tbl_rc_std_payments(std_id=std_id, txn_id=txn_id, invoice=invoice, amount=amount, type=type, mode=mode, remarks=remarks, date=pdate, status=status)
            data.save()

            query = tbl_rc_students.objects.get(id=std_id)
            if(query.regd_no == ''):
                query.regd_no = regdno
            if(query.roll_no == ''):
                query.roll_no = rollno
            query.save()
            del request.session['stdID']

            messages.success(request, 'Admission Successfully Done!')
            return redirect('manage_rc_student')
        else:
            stdID = request.session['stdID']
            stdInfo = tbl_rc_students.objects.get(id=stdID)
            streamInfo = tbl_rc_stream.objects.get(stream=stdInfo.stream, session=stdInfo.session, status='Active')
            stdCntData = tbl_rc_students.objects.filter(session=stdInfo.session, stream=stdInfo.stream).count()
            year = date.today().year
            nyear = str(year)[-2:]
            stream = stdInfo.stream
            nstream = stream[:3]

            if stdCntData < 10:
                rollno = stdCntData
                rollno = str(0) + str(0) + str(rollno)
            elif stdCntData < 100:
                rollno = stdCntData
                rollno = str(0) + str(rollno)

            rollnew = str(nyear) + str(nstream) + str(rollno)
            regdno = str(year) + str(19091319) + str(rollno)

            data = {'stdInfo':stdInfo, 'streamInfo':streamInfo, 'rollnew':rollnew, 'regdno':regdno, 'stdID':stdInfo.id}
            return render(request, 'dashboard/rc_student_admission_payment.html', data)
    else:
        return render(request, 'dashboard/404.html')

def std_payment_receipt(request, id):
    if tbl_rc_std_payments.objects.filter(id=id).exists():
        pinfo = tbl_rc_std_payments.objects.get(id=id)
        amount = pinfo.amount
        stdID = pinfo.std_id
        wamount = num2words(amount)
        stdInfo = tbl_rc_students.objects.get(id=stdID)
        data = {'pinfo':pinfo, 'stdInfo':stdInfo, 'wamount':wamount}
        return render(request, 'dashboard/receipt.html', data)
    else:
        return render(request, 'dashboard/404.html')

def student_icard(request, id):
    if tbl_rc_students.objects.filter(id=id).exists():
        stdInfo = tbl_rc_students.objects.get(id=id)
        data = {'stdInfo':stdInfo}
        return render(request, 'dashboard/student_idcard.html', data)
    else:
        return render(request, 'dashboard/404.html')

# Summer Course Stream Management 
@login_required(login_url='mylogin')
def manage_sc_stream(request):
    if request.method=='POST':
        stream = request.POST['stream']
        session = request.POST['session']
        duration = request.POST['duration']
        fees = request.POST['fees']
        status = 'Active'

        if tbl_sc_stream.objects.filter(stream=stream, session=session).exists():
            messages.error(request, 'Stream and session data can not be duplicate')
        else:
            data = tbl_sc_stream(stream=stream, session=session, duration=duration, fees=fees, status=status)
            data.save()
            messages.success(request, 'Data Successfully Saved!!')
        return redirect('manage_sc_stream')
    else:
        cyear = date.today().year
        nyear = date.today().year + 1
        sc_stream = tbl_sc_stream.objects.all().order_by('-id')
        data = {'sc_stream':sc_stream, 'cyear':cyear, 'nyear':nyear}
        return render(request, 'dashboard/manage_sc_stream.html', data)

@login_required(login_url='mylogin')
def update_sc_stream(request, id):
    update = tbl_sc_stream.objects.get(id=id)
    query = ScStreamForm(request.POST,request.FILES , instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_sc_stream')

@login_required(login_url='mylogin')
def update_sc_stream_status(request, id):
    query = tbl_sc_stream.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    return redirect('manage_sc_stream')

@login_required(login_url='mylogin')
def delete_sc_stream(request, id):
    db = tbl_sc_stream.objects.get(id=id)
    db.delete()
    return redirect('manage_sc_stream')

@login_required(login_url='mylogin')
def std_fees_information(request):
    if request.method=='POST':
        rollNo = request.POST['roll_no']
        if tbl_rc_students.objects.filter(roll_no=rollNo).exists():
            stdInfo = tbl_rc_students.objects.get(roll_no=rollNo)
            streamInfo = tbl_rc_stream.objects.get(stream=stdInfo.stream, session=stdInfo.session, status='Active')
            totalPaid = tbl_rc_std_payments.objects.filter(std_id=stdInfo.id).aggregate(ttlAmount=Sum('amount'))
            feesAmount = int(streamInfo.fees)
            paidAmount = int(totalPaid['ttlAmount'])
            remainingAmount = feesAmount - paidAmount
            data = {"stdInfo":stdInfo, "streamInfo":streamInfo, "paidAmount":paidAmount, "remainingAmount":remainingAmount, "rollNo":rollNo}
            messages.success(request, 'Student Roll no exist')
            return render(request, 'dashboard/rc_std_fees_payment.html', data)
        else:
            data = {"rollNo":rollNo}
            messages.error(request, 'Student Roll no was not exist in our records!!')
            return render(request, 'dashboard/rc_std_fees_payment.html', data)
    else:
        stdFees = tbl_rc_std_payments.objects.raw("select p.id, s.roll_no,p.invoice, p.txn_id from dashboard_tbl_rc_std_payments as p INNER JOIN dashboard_tbl_rc_students as s ON p.std_id=s.id")
        rollNo = tbl_rc_students.objects.filter(status='Active')
        data = {'stdFees':stdFees, 'rollNo':rollNo}
        return render(request, 'dashboard/std_fees_information.html', data)

@login_required(login_url='mylogin')
def rc_std_fees_payment(request):
    if request.method=='POST':
        std_id = request.POST['std_id']
        invoice = str(random.randint(1000000000, 9999999999))
        txn = str(random.randint(1000000000, 9999999999))
        txn_id = 'txn' + txn
        amount = request.POST['amount']
        type = request.POST['type']
        if type == 'OFFLINE':
            mode = request.POST['offline_mode']
        else:
            mode = request.POST['online_mode']
        remarks = request.POST['remarks']
        pdate = request.POST['date']
        status = 'active'

        data = tbl_rc_std_payments(std_id=std_id, txn_id=txn_id, invoice=invoice, amount=amount, type=type, mode=mode, remarks=remarks, date=pdate, status=status)
        data.save()
        return redirect('std_fees_information')

@login_required(login_url='mylogin')
def manage_sc_student(request):
    allStd = tbl_sc_students.objects.all().order_by('-id')
    data = {'allStd':allStd, 'ttlStd':allStd.count()}
    return render(request, 'dashboard/manage_sc_student.html', data)

@login_required(login_url='mylogin')
def add_sc_student(request):
    if request.method=='POST':
        roll_no = request.POST['roll_no']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        dob = request.POST['dob']
        aadhaar = request.POST['aadhaar']
        session = request.POST['session']
        stream = request.POST['stream']
        doj = request.POST['doj']
        std_photo = request.FILES['std_photo']
        guardian_name = request.POST['guardian_name']
        guardian_email = request.POST['guardian_email']
        guardian_mobile = request.POST['guardian_mobile']
        address = request.POST['address']
        matriculation_board = request.POST['matriculation_board']
        exceptation_marks = request.POST['exceptation_marks']
        status = 'Active'

        if tbl_sc_students.objects.filter(roll_no=roll_no, aadhaar=aadhaar).exists():
            messages.error(request, 'Roll No or Aadhaar No is exist!!')
        else:
            data = tbl_sc_students(roll_no=roll_no, name=name, email=email, mobile=mobile, gender=gender, dob=dob, aadhaar=aadhaar, session=session, stream=stream, doj=doj, guardian_name=guardian_name, guardian_email=guardian_email, guardian_mobile=guardian_mobile, address=address, matriculation_board=matriculation_board, exceptation_marks=exceptation_marks, std_photo=std_photo, status=status)
            data.save()

            laststdID = tbl_sc_students.objects.latest('id')
            request.session['summerStdID'] = laststdID.id
        return redirect('sc_student_payment')
    else:
        cyear = date.today().year
        nyear = date.today().year + 1
        session = str(cyear) + "-" + str(nyear)

        data = {'session':session}
        return render(request, 'dashboard/add_sc_student.html', data)

@login_required(login_url='mylogin')
def update_sc_student_status(request, id):
    query = tbl_sc_students.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    return redirect('manage_sc_student')

@login_required(login_url='mylogin')
def edit_sc_student(request, id):
    if tbl_sc_students.objects.filter(id=id).exists():
        query = tbl_sc_students.objects.get(id=id)
        data = {'query':query}
        return render(request, 'dashboard/edit_sc_student.html', data)
    else:
        return render(request, 'dashboard/404.html')

@login_required(login_url='mylogin')
def update_sc_student(request, id):
    update = tbl_sc_students.objects.get(id=id)
    stdData = ScStudentForm(request.POST or None, request.FILES, instance=update)
    stdData.save()
    if stdData.is_valid():
        stdData.save(commit=True)
        messages.success(request, 'Successfully Updated!')
    return redirect('manage_sc_student')

@login_required(login_url='mylogin')
def sc_student_payment(request):
    if 'summerStdID' in request.session:
        if request.method=='POST':
            std_id = request.POST['std_id']
            invoice = str(random.randint(1000000000, 9999999999))
            txn = str(random.randint(1000000000, 9999999999))
            txn_id = 'txn' + txn
            amount = request.POST['amount']
            type = request.POST['type']
            if type == 'OFFLINE':
                mode = request.POST['offline_mode']
            else:
                mode = request.POST['online_mode']
            remarks = request.POST['remarks']
            pdate = request.POST['date']
            status = 'active'

            data = tbl_sc_std_payments(std_id=std_id, txn_id=txn_id, invoice=invoice, amount=amount, type=type, mode=mode, remarks=remarks, date=pdate, status=status)
            data.save()
            del request.session['summerStdID']
            messages.success(request, 'Admission & Payment Successfully Done!')
            return redirect('manage_sc_student')
        else:
            summerStdID = request.session['summerStdID']
            stdInfo = tbl_sc_students.objects.get(id=summerStdID)
            streamInfo = tbl_sc_stream.objects.get(stream=stdInfo.stream, session=stdInfo.session, status='Active')

            data = {'stdInfo':stdInfo, 'streamInfo':streamInfo, 'stdID':stdInfo.id}
            return render(request, 'dashboard/sc_student_payment.html', data)
    else:
        return render(request, 'dashboard/404.html')

@login_required(login_url='mylogin')
def scstd_fees_information(request):
    if request.method=='POST':
        rollNo = request.POST['roll_no']
        if tbl_rc_students.objects.filter(roll_no=rollNo).exists():
            stdInfo = tbl_rc_students.objects.get(roll_no=rollNo)
            streamInfo = tbl_rc_stream.objects.get(stream=stdInfo.stream, session=stdInfo.session, status='Active')
            totalPaid = tbl_rc_std_payments.objects.filter(std_id=stdInfo.id).aggregate(ttlAmount=Sum('amount'))
            feesAmount = int(streamInfo.fees)
            paidAmount = int(totalPaid['ttlAmount'])
            remainingAmount = feesAmount - paidAmount
            data = {"stdInfo":stdInfo, "streamInfo":streamInfo, "paidAmount":paidAmount, "remainingAmount":remainingAmount, "rollNo":rollNo}
            messages.success(request, 'Student Roll no exist')
            return render(request, 'dashboard/rc_std_fees_payment.html', data)
        else:
            data = {"rollNo":rollNo}
            messages.error(request, 'Student Roll no was not exist in our records!!')
            return render(request, 'dashboard/rc_std_fees_payment.html', data)
    else:
        stdFees = tbl_sc_std_payments.objects.raw("select p.id, s.roll_no,p.invoice, p.txn_id from dashboard_tbl_sc_std_payments as p INNER JOIN dashboard_tbl_sc_students as s ON p.std_id=s.id")
        data = {'stdFees':stdFees}
        return render(request, 'dashboard/scstd_fees_information.html', data)

def scstd_payment_receipt(request, id):
    if tbl_sc_std_payments.objects.filter(id=id).exists():
        pinfo = tbl_sc_std_payments.objects.get(id=id)
        amount = pinfo.amount
        stdID = pinfo.std_id
        wamount = num2words(amount)
        stdInfo = tbl_sc_students.objects.get(id=stdID)
        data = {'pinfo':pinfo, 'stdInfo':stdInfo, 'wamount':wamount}
        return render(request, 'dashboard/scstd_receipt.html', data)
    else:
        return render(request, 'dashboard/404.html')