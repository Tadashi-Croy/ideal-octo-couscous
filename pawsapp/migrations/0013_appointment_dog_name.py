# Generated by Django 3.1.2 on 2020-11-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0012_remove_appointment_appt_dog'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='dog_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
