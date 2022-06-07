from logging import PlaceHolder
from pyexpat import model
from tkinter import Widget
from unicodedata import name
from attr import field, fields
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' :TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
        