# Generated by Django 3.1.6 on 2021-02-09 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_auto_20210209_0205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-date']},
        ),
    ]
