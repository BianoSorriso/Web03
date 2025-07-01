from django import forms

from django import forms
from django.core.exceptions import ValidationError
import re

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'id': 'nome'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'id': 'email'})
    )
    idade = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'id': 'idade'})
    )
    telefone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'id': 'telefone'})
    )