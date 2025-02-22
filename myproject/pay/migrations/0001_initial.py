# Generated by Django 5.1.4 on 2024-12-13 07:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('Account_number', models.CharField(max_length=12, unique=True)),
                ('Phone_number', models.CharField(max_length=10)),
                ('upi_id', models.CharField(max_length=15, unique=True)),
                ('Password', models.CharField(max_length=6)),
                ('Amount', models.CharField(max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_id', models.CharField(max_length=20, unique=True)),
                ('Recipeint', models.CharField(max_length=15)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Amount', models.CharField(max_length=6)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.user_account')),
            ],
        ),
    ]
