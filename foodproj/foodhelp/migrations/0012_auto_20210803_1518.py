# Generated by Django 3.2.5 on 2021-08-03 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0011_foodhelper_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foodhelper',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
