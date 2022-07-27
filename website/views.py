from django.shortcuts import render
from django.http import HttpResponse
from website.models import slider, sims

# Create your views here.
def index(request):
    allSlider = slider.objects.filter(status='Active')
    simsInfo = sims.objects.filter(id=1)
    data = {'allSlider':allSlider, 'simsInfo':simsInfo[0]}
    return render(request,'website/index.html', data)