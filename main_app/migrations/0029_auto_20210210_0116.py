# Generated by Django 3.1.6 on 2021-02-10 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_conversation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['-date']},
        ),
    ]
