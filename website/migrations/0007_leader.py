# Generated by Django 4.0.3 on 2022-07-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=500)),
                ('quotes', models.CharField(max_length=500)),
                ('about', models.TextField()),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('linkedin', models.CharField(max_length=500)),
                ('whatsapp', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
