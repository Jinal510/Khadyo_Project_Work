# Generated by Django 3.2.5 on 2021-08-05 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodhelp', '0027_rename_picup_address_addfood_pickup_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=10)),
                ('profile_pic', models.FileField(default='media/default.png', upload_to='img')),
                ('Address', models.TextField(blank=True, max_length=300)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.user')),
            ],
        ),
    ]