# Generated by Django 4.0.3 on 2022-07-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='image',
            field=models.ImageField(default='', upload_to='about/leader'),
        ),
    ]
