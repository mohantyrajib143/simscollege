from django.contrib import admin
from dashboard.models import password_token, tbl_rc_stream

# Register your models here.
admin.site.register(password_token)
admin.site.register(tbl_rc_stream)