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

class tbl_rc_students(models.Model):
    regd_no = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    aadhaar = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    doj = models.DateField()
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    guardian_relation = models.CharField(max_length=100)
    guardian_mobile = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    school_marks = models.CharField(max_length=100)
    school_info = models.CharField(max_length=200)
    present_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    aadhaar_card = models.ImageField(upload_to="students/aadhaar_card")
    std_photo = models.ImageField(upload_to="students/photo")
    std_document = models.ImageField(upload_to="students/documents")
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_rc_std_payments(models.Model):
    std_id = models.CharField(max_length=500)
    txn_id = models.CharField(max_length=500, default="")
    invoice = models.CharField(max_length=500, default="")
    amount = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    mode = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_sc_stream(models.Model):
    stream = models.CharField(max_length=500)
    session = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    fees = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)