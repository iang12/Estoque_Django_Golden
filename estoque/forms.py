#coding:utf-8
from django import forms
from django.forms import Select,Textarea,TextInput,NumberInput,EmailInput
from estoque.models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model   = Categoria
        exclude =['']
        fields  = '__all__'
        widgets = {
            'categoria': TextInput(attrs={'class':'form-control'})
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model   = Produto
        exclude = ['']
        fields  = '__all__'
        widgets={
            'produto': TextInput(attrs={'class': 'form-control','placeholder':'Digite o Nome Do Produto'}),
            'category': Select(attrs={'class': 'form-control'}),
            'fornecedor': Select(attrs={'class':'form-control'}),
            'estoque':NumberInput(attrs={'class':'form-control',}),
            'estoque_min':NumberInput(attrs={'class':'form-control',}),
            'ipi':NumberInput(attrs={'class':'form-control',}),
            'descricao':Textarea(attrs={'class':'form-control','rows':4}),
            'preco_compra':TextInput(attrs={'class': 'form-control','placeholder':'R$ 0,00'}),
            'preco_venda':TextInput(attrs={'class': 'form-control','placeholder':'R$ 0,00'}),
        }
class EntradaForm(forms.ModelForm):
    class Meta:
        model   = Entradas_Estoque
        exclude = ['']
        fields  = '__all__'
        widgets = {
            'categoria': Select(attrs={'class': 'form-control'}),
            'produto': Select(attrs={'class': 'form-control'}),
            'quantidade':TextInput(attrs={'class':'form-control','placeholder':'digite a quantidade '}),
            'observacao':Textarea(attrs={'class':'form-control','rows':3}),
        }