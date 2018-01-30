# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas_Estoque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(auto_now_add=True)),
                ('quantidade', models.DecimalField(blank=True, null=True, max_digits=13, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('observacao', models.TextField(blank=True)),
                ('categoria', models.ForeignKey(verbose_name=b'categoria', blank=True, to='estoque.Categoria', null=True)),
                ('produto', models.ForeignKey(blank=True, to='estoque.Produto', null=True)),
            ],
        ),
    ]
