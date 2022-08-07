from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import slider, sims, summer_course_enquiry, student_testmonials, about as AboutUs, leader, awards as Awards, faculties as AllFaculty, infrastructure, results, news as AllNews, notice, careers as AllCareers, JobApply, alumni_testmonials, contact as ContactSave
from college.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.
def index(request):
    msg={}
    if request.method=='POST':
        name = request.POST['name']
        emailid = request.POST['email']
        mobile = request.POST['mobile']
        stream = request.POST['stream']
        message = request.POST['message']

        data = summer_course_enquiry(name=name, email=emailid, mobile=mobile, stream=stream, message=message)
        data.save()

        email = 'mohantyrajib1998@gmail.com'

        html_content = render_to_string("website/admission_email.html",{'title':'New summer course applied','name':name, 'email':emailid, 'mobile':mobile, 'stream':stream, 'message':message})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "New Summer Course Applied At SIMS",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        if data.id != 0:
            msg = { "status": 1 } 
        return JsonResponse(msg)
    else:
        allSlider = slider.objects.filter(status='Active')
        stdTestmonial = student_testmonials.objects.all().order_by('-id')
        simsInfo = sims.objects.filter(id=1)
        data = {'allSlider':allSlider, 'simsInfo':simsInfo[0], 'stdTestmonial':stdTestmonial}
        return render(request,'website/index.html', data)

def about(request):
    aboutInfo = AboutUs.objects.filter(id=1)
    chairperson = leader.objects.filter(position='CHAIRPERSON')
    vicechairperson = leader.objects.filter(position='VICE CHAIRPERSON')
    principal = leader.objects.filter(position='PRINCIPAL')
    data = {'aboutInfo':aboutInfo[0], 'chairperson':chairperson[0], 'vicechairperson':vicechairperson[0], 'principal':principal[0]}
    return render(request, 'website/about.html', data)

def whyus(request):
    return render(request, 'website/whyus.html')

def awards(request):
    return render(request, 'website/awards.html')

def awards(request):
    awards = Awards.objects.all().order_by('-id')
    data = {'awards':awards}
    return render(request, 'website/awards.html', data)

def science(request):
    return render(request, 'website/science.html')

def commerce(request):
    return render(request, 'website/commerce.html')

def faculties(request):
    faculties = AllFaculty.objects.filter(type='CHSE',status='Active')
    data = {'faculties':faculties}
    return render(request, 'website/faculties.html', data)

def entrance(request):
    faculties = AllFaculty.objects.filter(type='ENTRANCE',status='Active')
    data = {'faculties':faculties}
    return render(request, 'website/entrance.html', data)

def chse(request):
    return render(request, 'website/chse.html')

def college(request):
    college = infrastructure.objects.filter(type='COLLEGE',status='Active')
    data = {'college':college}
    return render(request, 'website/college.html', data)

def hostel(request):
    hostel = infrastructure.objects.filter(type='HOSTEL',status='Active')
    data = {'hostel':hostel}
    return render(request, 'website/hostel.html', data)

def gallery(request):
    gallery = infrastructure.objects.filter(type='GALLERY',status='Active')
    data = {'gallery':gallery}
    return render(request, 'website/gallery.html', data)

def lab(request):
    lab = infrastructure.objects.filter(type='LAB',status='Active')
    data = {'lab':lab}
    return render(request, 'website/lab.html', data)

def sports(request):
    sports = infrastructure.objects.filter(type='SPORTS',status='Active')
    data = {'sports':sports}
    return render(request, 'website/sports.html', data)

def yoga(request):
    yoga = infrastructure.objects.filter(type='YOGA',status='Active')
    data = {'yoga':yoga}
    return render(request, 'website/yoga.html', data)

def neet(request):
    neet = results.objects.filter(type='NEET',status='Active')
    data = {'neet':neet}
    return render(request, 'website/neet.html', data)

def iit(request):
    iit = results.objects.filter(type='IIT',status='Active')
    data = {'iit':iit}
    return render(request, 'website/iit.html', data)

def chse_result(request):
    chse = results.objects.filter(type='CHSE',status='Active')
    data = {'chse':chse}
    return render(request, 'website/chse_result.html', data)

def news(request):
    news = AllNews.objects.filter(status='Active').order_by('-id')
    aboutInfo = AboutUs.objects.filter(id=1)
    data = {'news':news, 'aboutInfo':aboutInfo[0]}
    return render(request, 'website/news.html', data)

def notices(request):
    notices = notice.objects.filter(status='Active').order_by('-id')
    data = {'notices':notices}
    return render(request, 'website/notices.html', data)

def admission(request):
    msg={}
    if request.method=='POST':
        name = request.POST['name']
        emailid = request.POST['email']
        mobile = request.POST['mobile']
        stream = request.POST['stream']
        message = request.POST['message']

        data = summer_course_enquiry(name=name, email=emailid, mobile=mobile, stream=stream, message=message)
        data.save()

        email = 'mohantyrajib1998@gmail.com'

        html_content = render_to_string("website/admission_email.html",{'title':'New summer course applied','name':name, 'email':emailid, 'mobile':mobile, 'stream':stream, 'message':message})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "New Summer Course Applied At SIMS",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        if data.id != 0:
            msg = { "status": 1 } 
        return JsonResponse(msg)
    else:
        simsInfo = sims.objects.filter(id=1)
        data = {'simsInfo':simsInfo[0]}
        return render(request, 'website/admission.html', data)

def careers(request):
    careers = AllCareers.objects.filter(status='Active').order_by('-id')
    data = {'careers':careers}
    return render(request, 'website/careers.html', data)

def careers_info(request, id):
    msg={}
    if request.method=='POST':
        title = request.POST['title']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        resume = request.FILES['resume']
        message = request.POST['message']

        job = JobApply(title=title, name=name, email=email, mobile=mobile, resume=resume, message=message)
        job.save()

        if job.id != 0:
            msg = { "status": 1 } 
        return JsonResponse(msg)
    else:
        careerInfo = AllCareers.objects.filter(id=id)
        simsInfo = sims.objects.filter(id=1)
        data = {'careerInfo':careerInfo[0], 'simsInfo':simsInfo[0]}
        return render(request, 'website/careers_info.html', data)

def testimonial(request):
    stdTestmonial = student_testmonials.objects.all().order_by('-id')
    alumniTestmonial = alumni_testmonials.objects.all().order_by('-id')
    data = {'stdTestmonial':stdTestmonial, 'alumniTestmonial':alumniTestmonial}
    return render(request, 'website/testimonial.html', data)

def contact(request):
    msg={}
    if request.method=='POST':
        name = request.POST['name']
        emailid = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']

        data = ContactSave(name=name, email=emailid, contact=contact, subject=subject, message=message)
        data.save()

        email = 'mohantyrajib1998@gmail.com'

        html_content = render_to_string("website/contact_email.html",{'title':'New contact information added','name':name, 'email':emailid, 'contact':contact, 'subject':subject, 'message':message})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "New contact information added",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        if data.id != 0:
            msg = { "status": 1 } 
        return JsonResponse(msg)
    else:
        simsInfo = sims.objects.filter(id=1)
        data = {'simsInfo':simsInfo[0]}
        return render(request, 'website/contact.html', data)