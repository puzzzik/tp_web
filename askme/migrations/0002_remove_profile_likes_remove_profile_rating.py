# Generated by Django 4.1.3 on 2022-11-16 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rating',
        ),
    ]
