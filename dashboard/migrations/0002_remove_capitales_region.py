# Generated by Django 3.1.7 on 2021-03-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capitales',
            name='region',
        ),
    ]
