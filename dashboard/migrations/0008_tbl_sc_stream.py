# Generated by Django 4.0.3 on 2022-08-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_tbl_rc_students_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sc_stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=500)),
                ('session', models.CharField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('fees', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
