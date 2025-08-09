from django.db import models
from django.contrib.auth.models import User

class ConfiguracaoSite(models.Model):
    qr_code_pix = models.ImageField(upload_to='qr_codes/', verbose_name='QR Code PIX')
    chave_pix = models.CharField(max_length=255, verbose_name='Chave PIX')
    nome_beneficiario = models.CharField(max_length=255, verbose_name='Nome do Beneficiário')
    
    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configurações do Site'
    
    def __str__(self):
        return 'Configurações do Site'
    
    def save(self, *args, **kwargs):
        # Garantir que só exista uma instância
        if ConfiguracaoSite.objects.exists() and not self.pk:
            raise ValueError('Já existe uma configuração do site')
        return super().save(*args, **kwargs)

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
