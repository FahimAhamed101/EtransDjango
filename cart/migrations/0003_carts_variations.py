# Generated by Django 5.0.2 on 2024-02-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
        ('store', '0002_product_image4_product_is_featured_productgallery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]