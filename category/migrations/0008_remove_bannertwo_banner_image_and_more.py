# Generated by Django 5.1 on 2024-08-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_remove_bannertwo_banner_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannertwo',
            name='banner_image',
        ),
        migrations.AddField(
            model_name='bannertwo',
            name='banner_images',
            field=models.ImageField(blank=True, upload_to='photos/bannertwo'),
        ),
    ]
