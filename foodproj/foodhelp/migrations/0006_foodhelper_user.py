# Generated by Django 3.2.5 on 2021-07-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodhelp', '0005_auto_20210730_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('confirmpassword', models.CharField(max_length=25)),
                ('otp', models.IntegerField(default=459)),
                ('role', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foodhelper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhelp.user')),
            ],
        ),
    ]