# Generated by Django 3.1.6 on 2021-02-05 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0007_auto_20210205_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seed',
            name='users',
        ),
        migrations.AddField(
            model_name='seed',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
