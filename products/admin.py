from django.contrib import admin
from .models import Product, Offer,Category


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
