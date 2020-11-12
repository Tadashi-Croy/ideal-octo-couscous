# Generated by Django 3.1.2 on 2020-10-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='Portland', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='Oregon', max_length=75),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default='00000', max_length=10),
        ),
    ]