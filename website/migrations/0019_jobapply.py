# Generated by Django 4.0.3 on 2022-08-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_careers'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=500)),
                ('resume', models.ImageField(upload_to='resume')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]