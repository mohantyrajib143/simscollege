from django.contrib import admin
from dashboard.models import password_token, tbl_rc_stream, tbl_rc_students, tbl_rc_std_payments, tbl_sc_stream

# Register your models here.
admin.site.register(password_token)
admin.site.register(tbl_rc_stream)
admin.site.register(tbl_rc_students)
admin.site.register(tbl_rc_std_payments)
admin.site.register(tbl_sc_stream)