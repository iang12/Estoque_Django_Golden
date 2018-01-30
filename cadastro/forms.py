#coding:utf-8
from django import forms
from django.forms import Select,Textarea,TextInput,NumberInput,EmailInput,DateInput
from cadastro.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model   = Cliente
        exclude = ['']
        fields  = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control','placeholder':'Nome e Sobrenome'}),
            'nascimento': DateInput(attrs={'class': 'form-control','placeholder':'dd/mm/aaaa'}),
            'sexo': Select(attrs={'class':'form-control'}),
            'cpf':TextInput(attrs={'class':'form-control','placeholder':'digite seu CPF'}),
            'telefone':TextInput(attrs={'class':'form-control','placeholder':'digite seu telefone'}),
            'email':TextInput(attrs={'class':'form-control','placeholder':'digite seu E-mail'}),
            'instagran':TextInput(attrs={'class':'form-control','placeholder':'Instagran'}),
	        

    }
    class Media:
        css = {
        'all': ('css/admin.css',)
        }
        
        js = ('jquery-1.8.3.min.js')
        js = ('jquery.maskedinput.min.js',)
        js = ('admin.js')