# Generated by Django 3.2.5 on 2021-08-14 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0030_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addfood',
            name='fid',
        ),
        migrations.RemoveField(
            model_name='addfood',
            name='person_type',
        ),
        migrations.RemoveField(
            model_name='addfood',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='foodhelper',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='ngo',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='AddFood',
        ),
        migrations.DeleteModel(
            name='foodhelper',
        ),
        migrations.DeleteModel(
            name='NGO',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]