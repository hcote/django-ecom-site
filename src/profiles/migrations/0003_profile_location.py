# Generated by Django 2.0.5 on 2018-08-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my default location', max_length=120),
        ),
    ]