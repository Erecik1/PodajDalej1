from django import forms

from .models import Product

class ProForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'describe','category','image')

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50, label='Imię')
	last_name = forms.CharField(max_length = 50, label='Nazwisko')
	email_address = forms.EmailField(max_length = 150, label='Email')
	message = forms.CharField(widget = forms.Textarea, max_length = 2000, label="Wiadomość")