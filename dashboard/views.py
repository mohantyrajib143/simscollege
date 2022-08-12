from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from website.models import slider, about
from django.contrib import messages
from . forms import SliderForm, AboutForm

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
        messages.success(request, 'Successfully Updated!')
    return redirect('manage_slider')

def update_slider_status(request, id):
    query = slider.objects.get(id=id)
    if(query.status == 'Active'):
        query.status = 'Inactive'
    else:
        query.status = 'Active'
    query.save()
    messages.success(request, 'Successfully Updated!')
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
        messages.success(request, 'Successfully Updated!')
    return redirect('manage_aboutus')


    # if request.method=='POST':
    #     title = request.POST['title']
    #     image = request.FILES['image']
    #     status = 'Active'

    #     data = slider(title=title, image=image, status=status)
    #     data.save()
    #     messages.success(request, 'Data Successfully Saved!!')
    #     return redirect('manage_slider')
    # else:
    #     query = about.objects.filter(id=id)
    #     data = {'query':query[0]}
    #     return render(request, 'dashboard/manage_aboutus.html', data)









        # if about.objects.filter(id=id).exists():
    #     update = about.objects.get(id=id)
    #     query = AboutForm(request.POST, instance=update)
    #     query.save()
    #     if query.is_valid():
    #         query.save(commit=True)
    #         messages.success(request, 'Successfully Updated!')
    #     return redirect('manage_admission_query')
    # else: