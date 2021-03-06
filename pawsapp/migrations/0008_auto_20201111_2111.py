# Generated by Django 3.1.2 on 2020-11-12 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_userprofile_share_pupps'),
        ('pawsapp', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_appt1', models.DateTimeField(blank=True, null=True)),
                ('req_appt2', models.DateTimeField(blank=True, null=True)),
                ('req_appt3', models.DateTimeField(blank=True, null=True)),
                ('appt_dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.dog')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='dog_info',
            name='dog_owner',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Dog_info',
        ),
    ]
