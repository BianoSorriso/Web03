# Generated by Django 5.1.3 on 2025-05-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_delete_qrcodedoacao"),
    ]

    operations = [
        migrations.CreateModel(
            name="QRCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("imagem", models.ImageField(upload_to="qrcodes/")),
                ("chave_pix", models.CharField(max_length=200)),
            ],
        ),
    ]
