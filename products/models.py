from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nazwa produktu")
    price = models.FloatField(verbose_name="Cena produktu")
    stock = models.IntegerField(verbose_name="Sztuki")
    describe = models.CharField(max_length=255, null=True, verbose_name="Opis produktu")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Kategoria")
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name="Zdjęcie produktu")

    def __str__(self):
        return self.name 


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
