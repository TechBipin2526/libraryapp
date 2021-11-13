from django import forms
from django.forms import fields
from .models import Book

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'