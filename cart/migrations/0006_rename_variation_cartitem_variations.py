# Generated by Django 5.0.2 on 2024-02-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_rename_variations_cartitem_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]
