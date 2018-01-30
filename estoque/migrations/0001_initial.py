# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, unique=True)),
                ('criado', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100, unique=True, verbose_name=b'Produto')),
                ('importado', models.BooleanField(default=False, verbose_name=b'Importado')),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=7, verbose_name=b'Pre\xc3\xa7o De Venda')),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=7, verbose_name=b'Pre\xc3\xa7o De Compra')),
                ('ipi', models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name=b'IPI')),
                ('estoque', models.IntegerField(default=0, verbose_name=b'Estoque atual')),
                ('estoque_min', models.PositiveIntegerField(default=0, verbose_name=b'Estoque m\xc3\xadnimo')),
                ('descricao', models.CharField(max_length=300, verbose_name=b'Observa\xc3\xa7\xc3\xa3o')),
                ('data_de_cadastro', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.Categoria', verbose_name=b'categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
