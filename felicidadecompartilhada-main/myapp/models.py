from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Filial(models.Model):
    UNIDADE_1 = ''
    UNIDADE_2 = ''
    UNIDADE_CHOICE = ((UNIDADE_1,''),(UNIDADE_2,''))

    nome_filial = models.CharField(max_length=100,choices=UNIDADE_CHOICE,null=True,blank=True)

    def __str__(self):
        return self.nome_filial


"""class Necessidade_especial(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao"""





class Atividade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cadastro das atividades"

    def __str__(self):
        return self.nome


class Instituicao(models.Model):
    nome_da_instituicao = models.CharField(max_length=50)
    tempo_de_fundacao = models.IntegerField(blank=True, null=True, verbose_name="Tempo de fundação (em anos)")
    cnpj = models.CharField(max_length=14)
    publico_alvo = models.CharField(max_length=100, blank=True)
    capacidade = models.IntegerField (blank=True, null=True)
    link_abrigo = models.CharField(max_length=300)



    class Meta:
        verbose_name_plural = "Cadastro de Abrigos"

    def __str__(self):
        return self.nome_da_instituicao



# REMOVIDO
"""class Participacao(models.Model):
    nome = models.ForeignKey(Crianca, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default="INSCRITA")

    class Meta:
        verbose_name_plural = "Participações das crianças"

    def nome_crianca(self):
        return self.nome.nome
    nome_crianca.admin_order_field = 'nome'
    nome_crianca.short_description = 'Nome da Criança'"""




class RelatorioAnual(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='relatorios_imagens/')
    link_relatorio = models.URLField(max_length=500, blank=True, null=True)
    ano = models.IntegerField()

    def __str__(self):
        return f"Relatório {self.ano}"


class QRCodePixFelicidade(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, primary_key=True)
    imagem = models.ImageField(upload_to='doacaoFelicidade/')

    def __str__(self):
        return self.email

    def clean(self):
        if not self.pk and QRCodePixFelicidade.objects.exists():
            raise ValidationError('Já existe um Pix cadastrado. Para fazer mudanças, altere o Pix existente.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Doação Pix QR Code (Felicidade Compartilhada)"
        verbose_name_plural = "Doação Pix QR Code (Felicidade Compartilhada)"
        
class QRCodePixParceiros(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='doacaoParceiros/')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Doação Pix QR Code (Parceiros)"
        verbose_name_plural = "Doação Pix QR Code (Parceiros)"