# Generated by Django 3.2.5 on 2021-08-03 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0009_auto_20210803_1245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foodhelper',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
