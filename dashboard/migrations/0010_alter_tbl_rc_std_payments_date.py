# Generated by Django 4.0.3 on 2022-08-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_tbl_rc_std_payments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_rc_std_payments',
            name='date',
            field=models.CharField(max_length=500),
        ),
    ]
