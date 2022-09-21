from django.shortcuts import render
from django.http import JsonResponse
from website.models import slider
from . serializers import SliderSerializer

# Create your views here.
def sliderList(request):
    allSlider = slider.objects.filter(status='Active')
    serializer = SliderSerializer(allSlider, many=True)
    return JsonResponse(serializer.data, safe=False)
