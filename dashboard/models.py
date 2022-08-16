from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class password_token(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class tbl_rc_stream(models.Model):
    stream = models.CharField(max_length=500)
    session = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    fees = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return ' New Stream Added Named ' + self.stream