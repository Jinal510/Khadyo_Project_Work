# Generated by Django 3.2.5 on 2021-08-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0017_addfood_foodhelper_user_userrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='addfood',
            name='food_categories',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
