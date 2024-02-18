# Generated by Django 5.0.2 on 2024-02-18 06:50

import django.core.validators
import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['product_name'], unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('offer_price', models.IntegerField(blank=True, null=True)),
                ('offer_perc', models.IntegerField(blank=True, default=0, null=True)),
                ('image1', models.ImageField(upload_to='photos/products')),
                ('image2', models.ImageField(blank=True, upload_to='photos/products')),
                ('image3', models.ImageField(blank=True, upload_to='photos/products')),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('product_offer', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Is_offer_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]