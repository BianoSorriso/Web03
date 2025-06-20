# Generated by Django 5.1.3 on 2025-05-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_qrcodedoacao_alter_instituicao_capacidade_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="qrcodedoacao",
            old_name="qrcode",
            new_name="imagem",
        ),
        migrations.AddField(
            model_name="qrcodedoacao",
            name="principal",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="qrcodedoacao",
            name="chave_pix",
            field=models.CharField(max_length=100),
        ),
    ]
