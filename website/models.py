from django.db import models

# Create your models here.
SLIDER_STATUS_CHOICES = (
       ('Active','Active'),
       ('Inactive', 'Inactive'),
    )
class slider(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="home/slider")
    status = models.CharField(max_length=500, choices=SLIDER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ' added new slider '
    
class sims(models.Model):
    about = models.CharField(max_length=500)
    description = models.TextField()
    email1 = models.CharField(max_length=200)
    email2 = models.CharField(max_length=200)
    contact1 = models.CharField(max_length=200)
    contact2 = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    whatsapp1 = models.CharField(max_length=200)
    whatsapp2 = models.CharField(max_length=200)
    science_std = models.CharField(max_length=200)
    commerce_std = models.CharField(max_length=200)
    total_teacher = models.CharField(max_length=200)
    graduate_std = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' SIMS college information details '

class summer_course_enquiry(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    stream = models.CharField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' Summer Course Enquiry Added By ' + self.name