# Generated by Django 3.2.5 on 2021-07-30 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0004_foodhelper_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foodhelper',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]