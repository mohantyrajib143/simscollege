from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import slider, sims, summer_course_enquiry, student_testmonials, about as AboutUs, leader, awards as Awards, faculties as AllFaculty, infrastructure, results

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