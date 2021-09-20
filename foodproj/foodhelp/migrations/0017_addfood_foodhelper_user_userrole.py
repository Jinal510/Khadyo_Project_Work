# Generated by Django 3.2.5 on 2021-08-04 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodhelp', '0016_auto_20210804_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('otp', models.IntegerField(default=459)),
                ('role', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='foodhelper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=10)),
                ('profile_pic', models.FileField(default='media/default.png', upload_to='img')),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.user')),
            ],
        ),
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
                ('zipcode', models.CharField(max_length=20)),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.foodhelper')),
                ('person_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.userrole')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.user')),
            ],
        ),
    ]