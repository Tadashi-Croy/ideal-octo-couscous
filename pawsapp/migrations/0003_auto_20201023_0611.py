# Generated by Django 3.1.2 on 2020-10-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0002_auto_20201023_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='req_appt1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='req_appt2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='req_appt3',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]