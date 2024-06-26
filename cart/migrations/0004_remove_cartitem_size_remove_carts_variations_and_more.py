# Generated by Django 5.0.2 on 2024-02-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_carts_variations'),
        ('store', '0002_product_image4_product_is_featured_productgallery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
        migrations.RemoveField(
            model_name='carts',
            name='variations',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
