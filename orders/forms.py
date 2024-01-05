from django import forms
from django.forms import TextInput, EmailInput
from django.views import View

from orders.models import Order
from products.models import User


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Ivan',
                                                         'value': '', 'required': True}))
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Ivanov',
                                                        'value': '', 'required': True}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com',
                                                      'value': '', 'required': True}))
    address = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Ukraine, Kharkov, Sumska, 100',
                                'required': True}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address']
