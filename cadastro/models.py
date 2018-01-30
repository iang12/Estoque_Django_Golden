from django.db import models
from cadastro.choices import *

class Cliente(models.Model):
    nome       = models.CharField('Nome', max_length=35)
    cpf        = models.CharField('CPF', max_length=15,unique=True, null=True, blank=True)
    sexo       = models.CharField('Sexo', max_length=1, choices=SEXO,blank=True) 
    nascimento = models.DateField('Data De Nascimento')
    email      = models.EmailField('E-mail',max_length=30,blank=True)
    telefone   = models.CharField('Telefone',max_length=20,blank=True)
    instagran  = models.CharField('Instagran',max_length=20,blank=True)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome 
