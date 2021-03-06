# Generated by Django 3.2.2 on 2021-06-06 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210125_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.category', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='describe',
            field=models.CharField(max_length=255, null=True, verbose_name='Opis produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=2083, verbose_name='Url zdjęcia'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Cena produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='Sztuki'),
        ),
    ]
