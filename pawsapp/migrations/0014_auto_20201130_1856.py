# Generated by Django 3.1.2 on 2020-12-01 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0013_appointment_dog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.CharField(default=datetime.datetime(2020, 12, 1, 2, 56, 49, 524459, tzinfo=utc), max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='replied_to',
            field=models.BooleanField(default=False),
        ),
    ]
