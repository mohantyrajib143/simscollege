from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import slider, sims, summer_course_enquiry, student_testmonials, about as AboutUs, leader, awards as Awards

# Create your views here.
def index(request):
    msg={}
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        stream = request.POST['stream']
        message = request.POST['message']

        data = summer_course_enquiry(name=name, email=email, mobile=mobile, stream=stream, message=message)
        data.save()

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