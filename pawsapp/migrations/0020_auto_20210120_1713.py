# Generated by Django 3.1.2 on 2021-01-21 01:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0019_auto_20210120_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.CharField(default=datetime.datetime(2021, 1, 21, 1, 13, 19, 994404, tzinfo=utc), max_length=100),
        ),
    ]
