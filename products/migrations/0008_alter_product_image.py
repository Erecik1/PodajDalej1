# Generated by Django 3.2.2 on 2021-06-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_image_url_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Zdjęcie produktu'),
        ),
    ]