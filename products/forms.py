from django import forms

from .models import Product

class ProForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'describe','category','image_url')