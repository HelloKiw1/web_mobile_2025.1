# Generated by Django 5.2 on 2025-05-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0005_receita_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='receita/fotos'),
        ),
    ]
