from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'marca']

class CustomUserForm(UserCreationForm):
    pass