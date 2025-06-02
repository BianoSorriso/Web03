from django import forms

from django import forms
from django.core.exceptions import ValidationError

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


    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if any(char.isdigit() for char in nome):
            raise ValidationError("O nome não pode conter números.")
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if any(char.isalpha() for char in telefone):
            raise ValidationError("O telefone não pode conter letras.")
        return telefone



    def clean_idade(self):
        idade = self.cleaned_data['idade']
        if idade < 18:
            raise ValidationError("Você precisa ter pelo menos 18 anos para se voluntariar.")
        return idade
