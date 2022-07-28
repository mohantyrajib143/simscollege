# Generated by Django 4.0.3 on 2022-07-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_summer_course_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_testmonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='home/student_testmonials')),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]