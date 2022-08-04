# Generated by Django 4.0.3 on 2022-08-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('experience', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='about/awards')),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('linkedin', models.CharField(max_length=500)),
                ('whatsapp', models.CharField(max_length=500)),
                ('gmail', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
