# Generated by Django 3.2.5 on 2021-08-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0028_ngo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngo',
            old_name='Address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='ngo',
            name='profile_pic',
            field=models.FileField(blank=True, default='media/default.png', upload_to='img'),
        ),
    ]
