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