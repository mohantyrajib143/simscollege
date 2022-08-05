from email.policy import default
from turtle import position
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

STD_TESTMONIAL_STATUS_CHOICES = (
       ('Active','Active'),
       ('Inactive', 'Inactive'),
    )
class student_testmonials(models.Model):
    name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    image = models.ImageField(upload_to="home/student_testmonials")
    message = models.TextField()
    status = models.CharField(max_length=500, choices=STD_TESTMONIAL_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' New Testmonial Added By ' + self.name

class about(models.Model):
    about = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    features = models.TextField()
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    whatsapp = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    telegram = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' SIMS college about information details '

class leader(models.Model):
    name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    image = models.ImageField(upload_to="about/leader", default="")
    quotes = models.CharField(max_length=500)
    about = models.TextField()
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    whatsapp = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.position + ' INFORMATION' 

class awards(models.Model):
    title = models.CharField(max_length=500)
    award = models.CharField(max_length=500)
    image = models.ImageField(upload_to="about/awards")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' New awards added by ' + self.title

FAC_STATUS_CHOICES = (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
)
class faculties(models.Model):
    type = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    image = models.ImageField(upload_to="academics/faculties")
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    whatsapp = models.CharField(max_length=500)
    gmail = models.CharField(max_length=500)
    status = models.CharField(max_length=500, choices=FAC_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type + ' faculties added named ' + self.name

INFRASTRUCTURE_STATUS_CHOICES = (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
)
class infrastructure(models.Model):
    type = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to="infrastructure")
    status = models.CharField(max_length=500, choices=INFRASTRUCTURE_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type + ' infrastructure added with title ' + self.title

RESULT_STATUS_CHOICES = (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
)
class results(models.Model):
    type = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    position = models.TextField()
    image = models.ImageField(upload_to="results")
    status = models.CharField(max_length=500, choices=RESULT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + ' achived ' + self.type

NEWS_STATUS_CHOICES = (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
)
class news(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to="news")
    status = models.CharField(max_length=500, choices=NEWS_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

NOTICE_STATUS_CHOICES = (
    ('Active','Active'),
    ('Inactive', 'Inactive'),
)
class notice(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    status = models.CharField(max_length=500, choices=NOTICE_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title