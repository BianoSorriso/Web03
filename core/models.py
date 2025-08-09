from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Voluntario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    area_interesse = models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario.username

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} - {self.assunto}"

class Doacao(models.Model):
    TIPO_CHOICES = (
        ('dinheiro', 'Dinheiro'),
        ('alimentos', 'Alimentos'),
        ('roupas', 'Roupas'),
        ('outros', 'Outros'),
    )
    
    nome_doador = models.CharField(max_length=100)
    email_doador = models.EmailField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_doacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome_doador} - {self.tipo}"
