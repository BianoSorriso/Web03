from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.
class Evento(models.Model):
  nome = models.CharField(max_length=200)
  data = models.DateField()
  hora = models.TimeField()
  Pix = models.CharField(max_length=255, null=True, blank=True)
  imagem = models.ImageField(upload_to='eventos/')
  link_postagem = models.CharField(max_length=300)
  info = models.TextField()
  
  def __str__(self):
    return self.nome
  

def validar_idade_minima(value):
    if value < 18:
        raise ValidationError('A idade mínima para voluntários é 18 anos.')

class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField(null=True, blank=True, validators=[validar_idade_minima])  # Validador adicionado
    telefone = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nome