# Generated by Django 5.0.2 on 2024-02-18 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], default='M', max_length=10, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carts_id', models.CharField(blank=True, max_length=150)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('coupon_applied', models.CharField(blank=True, default=0, max_length=30, null=True)),
                ('final_offer_price', models.FloatField(blank=True, default=0, null=True)),
                ('user', models.EmailField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=30, unique=True)),
                ('valid_from', models.DateTimeField(null=True)),
                ('valid_to', models.DateTimeField(null=True)),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-valid_to'],
            },
        ),
        migrations.CreateModel(
            name='Paymentrazor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(blank=True, max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('payment_signature', models.CharField(blank=True, max_length=100)),
                ('total_amount', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('ACCEPTED', 'ACCEPTED'), ('FAILED', 'FAILED')], max_length=50)),
            ],
        ),
    ]
