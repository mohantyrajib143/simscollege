from django.shortcuts import render
from django.http import JsonResponse
from website.models import slider
from django.contrib.auth.models import User
from . serializers import SliderSerializer, UserSerializer

# Create your views here.
def sliderList(request):
    allSlider = slider.objects.filter(status='Active')
    serializer = SliderSerializer(allSlider, many=True)
    return JsonResponse(serializer.data, safe=False)

def userList(request):
    allUser = User.objects.all()
    serializer = UserSerializer(allUser, many=True)
    return JsonResponse(serializer.data, safe=False)