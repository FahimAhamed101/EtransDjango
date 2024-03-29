# Generated by Django 5.0.2 on 2024-02-18 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='profile/avatar.png', max_length=500, upload_to='profile/')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('Phone_number', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('MEN', 'MEN'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='Male', max_length=10)),
                ('house', models.CharField(max_length=50, null=True)),
                ('town', models.CharField(max_length=50, null=True)),
                ('locality', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('Address_type', models.CharField(choices=[('HOME', 'HOME'), ('OFFICE', 'OFFICE'), ('OTHERS', 'OTHERS')], default='HOME', max_length=10)),
                ('zip', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, max_length=20, null=True)),
                ('is_applied', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
