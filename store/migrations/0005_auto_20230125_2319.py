# Generated by Django 3.1 on 2023-01-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20230120_1538'),
        ('orders', '0001_initial'),
        ('store', '0004_productgallery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Variations',
            new_name='Variation',
        ),
    ]