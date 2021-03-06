# Generated by Django 3.2.5 on 2021-08-04 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0013_foodhelper_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('foodquantity', models.CharField(max_length=20)),
                ('foodquality', models.CharField(max_length=20)),
                ('cooktime', models.CharField(max_length=20)),
                ('expirytime', models.CharField(max_length=20)),
                ('food_picture', models.FileField(upload_to='media/img/')),
                ('food_video', models.FileField(upload_to='media/video/')),
                ('picture_address', models.CharField(max_length=50)),
                ('contact_person_name', models.CharField(max_length=20)),
                ('contact_person_number', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.user')),
            ],
        ),
    ]
