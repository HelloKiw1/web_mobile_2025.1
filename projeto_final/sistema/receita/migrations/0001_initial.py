# Generated by Django 5.2 on 2025-04-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.SmallIntegerField(choices=[(1, 'CAFE DA MANHA'), (2, 'LANCHE'), (3, 'ALMOÇO'), (4, 'JANTA'), (5, 'OUTRO')])),
                ('cor', models.SmallIntegerField(choices=[(1, 'DOCE'), (2, 'SALGADO'), (3, 'OUTRO')])),
            ],
        ),
    ]
