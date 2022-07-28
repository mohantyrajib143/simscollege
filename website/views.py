from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import slider, sims, summer_course_enquiry

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
        simsInfo = sims.objects.filter(id=1)
        data = {'allSlider':allSlider, 'simsInfo':simsInfo[0]}
        return render(request,'website/index.html', data)