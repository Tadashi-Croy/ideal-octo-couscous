# Generated by Django 3.1.2 on 2020-11-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsapp', '0010_auto_20201116_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appt_dog',
            field=models.CharField(blank=True, default='GET RID OF ME', max_length=500, null=True),
        ),
    ]