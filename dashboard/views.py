from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from website.models import slider, about, leader, awards, student_testmonials, alumni_testmonials, faculties, infrastructure, results, news
from django.contrib import messages
from . forms import SliderForm, AboutForm, LeaderForm, AwardForm, StdTestimonialForm, AlumniTestimonialForm, ChseFacultyForm, InfrastructureForm, ResultsForm, NewsForm

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

def update_chse_faculty_status(request, id):
    query = faculties.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_chse_faculty')

def delete_chse_faculty(request, id):
    db = faculties.objects.get(id=id)
    file = faculties.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_chse_faculty')

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

def update_entrance_faculty_status(request, id):
    query = faculties.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_entrance_faculty')

def delete_entrance_faculty(request, id):
    db = faculties.objects.get(id=id)
    file = faculties.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_entrance_faculty')

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

def update_college_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_college')

def delete_college(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_college')

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

def update_hostel_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_hostel')

def delete_hostel(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_hostel')

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

def update_gallery_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_gallery')

def delete_gallery(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_gallery')


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

def update_labs_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_labs')

def delete_labs(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_labs')

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

def update_sports_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_sports')

def delete_sports(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_sports')

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

def update_yoga_status(request, id):
    query = infrastructure.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_yoga')

def delete_yoga(request, id):
    db = infrastructure.objects.get(id=id)
    file = infrastructure.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_yoga')

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

def update_neet_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_neet')

def delete_neet(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_neet')

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

def update_iit_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_iit')

def delete_iit(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_iit')

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

def update_chse_status(request, id):
    query = results.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_chse')

def delete_chse(request, id):
    db = results.objects.get(id=id)
    file = results.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_chse')

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

def update_news_status(request, id):
    query = news.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Status Successfully Updated!')
    return redirect('manage_news')

def delete_news(request, id):
    db = news.objects.get(id=id)
    file = news.objects.get(id=id).image.delete(save=True)
    db.delete()
    messages.success(request, 'Data Successfully Deleted!!')
    return redirect('manage_news')