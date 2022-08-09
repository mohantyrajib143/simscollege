from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'dashboard/login.html')

def forgot_pass(request):
    return render(request, 'dashboard/forgot_pass.html')