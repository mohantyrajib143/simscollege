# Generated by Django 4.0.3 on 2022-09-15 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_delete_tbl_sc_stream'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_rc_std_payments',
        ),
    ]