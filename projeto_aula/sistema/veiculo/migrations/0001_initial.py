# Generated by Django 5.2 on 2025-04-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.SmallIntegerField(choices=[(1, 'AUDI'), (2, 'BMW'), (3, 'CHEVROLET - GM'), (4, 'FERRARI')])),
                ('combustivel', models.SmallIntegerField(choices=[(1, 'ETANOL'), (2, 'GASOLINA'), (3, 'FLEX'), (4, 'DIESEL'), (5, 'ELETRICO')])),
                ('cor', models.SmallIntegerField(choices=[(1, 'Preto'), (2, 'Vermelho'), (3, 'Branco')])),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
