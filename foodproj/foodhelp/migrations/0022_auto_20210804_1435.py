# Generated by Django 3.2.5 on 2021-08-04 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0021_rename_picture_address_addfood_pickup_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodhelper',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='AddFood',
        ),
        migrations.DeleteModel(
            name='foodhelper',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
