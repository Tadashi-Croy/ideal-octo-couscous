# Generated by Django 3.1.2 on 2020-11-11 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='tester',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
