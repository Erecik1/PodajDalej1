# Generated by Django 3.2.2 on 2021-06-14 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='image',
        ),
    ]
