# Generated by Django 3.0.8 on 2020-07-09 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('be_app', '0004_auto_20200709_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]