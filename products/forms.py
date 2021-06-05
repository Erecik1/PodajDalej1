from django import forms

from .models import Product

class ProForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'describe','category','image_url')

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)