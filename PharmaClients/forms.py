from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import DrugOrder, Delivery

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name'
        ]
class OrderForm(forms.ModelForm):
    class Meta:
        model = DrugOrder
        fields = ['Quantity',]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'Country', 'City', 'Street_Name', 'House_No'
        ]


