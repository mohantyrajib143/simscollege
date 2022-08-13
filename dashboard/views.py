from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from website.models import slider, about, leader, awards, student_testmonials, alumni_testmonials
from django.contrib import messages
from . forms import SliderForm, AboutForm, LeaderForm, AwardForm, StdTestimonialForm, AlumniTestimonialForm

# Create your views here.
def login(request):
    return render(request, 'dashboard/login.html')

def forgot_pass(request):
    return render(request, 'dashboard/forgot_pass.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

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

def update_slider_status(request, id):
    query = slider.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_slider')

def delete_slider(request, id):
    db = slider.objects.get(id=id)
    file = slider.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_slider')

def manage_aboutus(request):
    query = about.objects.filter(id=1)
    data = {'query':query[0]}
    return render(request, 'dashboard/manage_aboutus.html', data)

def update_aboutus(request):
    update = about.objects.get(id=1)
    query = AboutForm(request.POST, instance=update)
    query.save()
    if query.is_valid():
        query.save(commit=True)
        messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_aboutus')

def manage_leader(request):
    allLeader = leader.objects.all()
    data = {'allLeader':allLeader}
    return render(request, 'dashboard/manage_leader.html', data)

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

def delete_awards(request, id):
    db = awards.objects.get(id=id)
    file = awards.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_awards')

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

def update_stdtestimonial_status(request, id):
    query = student_testmonials.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Data Successfully Updated!')
    return redirect('manage_stdtestimonial')

def delete_stdtestimonial(request, id):
    db = student_testmonials.objects.get(id=id)
    file = student_testmonials.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_stdtestimonial')

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

def update_alumni_testimonial_status(request, id):
    query = alumni_testmonials.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_alumni_testimonial')

def delete_alumni_testimonial(request, id):
    db = alumni_testmonials.objects.get(id=id)
    file = alumni_testmonials.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_alumni_testimonial')