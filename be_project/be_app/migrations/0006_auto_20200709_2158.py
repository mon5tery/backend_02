# Generated by Django 3.0.8 on 2020-07-09 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be_app', '0005_auto_20200709_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
