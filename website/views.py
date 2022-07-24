from django.shortcuts import render
from django.http import HttpResponse
from website.models import slider

# Create your views here.
def index(request):
    allSlider = slider.objects.filter(status='Active')
    data = {'allSlider':allSlider}
    return render(request,'website/index.html', data)