# Generated by Django 4.0.3 on 2022-08-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_leader_address_remove_leader_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('award', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='about/awards')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]