# Generated by Django 4.0.3 on 2022-08-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_faculties_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='infrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('information', models.TextField()),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='infrastructure')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
