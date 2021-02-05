# Generated by Django 3.1.6 on 2021-02-05 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_auto_20210205_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.TextField(max_length=500)),
                ('seed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.seed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
