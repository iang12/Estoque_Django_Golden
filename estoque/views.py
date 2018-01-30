# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from estoque.models import *
from estoque.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.template.loader import render_to_string

#######################Categorias##########################
class ListaCategoria(ListView):
    context_object_name = 'categorias'
    model = Categoria
    template_name = 'categorias/categorias.html'

class Detalhes( DetailView):
    model = Categoria
    template_name = 'categorias/detalhes.html'

class Add_Categoria(CreateView):
    form_class = CategoriaForm
    template_name = 'categorias/includes/add_categoria.html'
    model = Categoria
    success_url='/categorias'

class Categoria_Detalhes(DetailView):
    model = Categoria
    template_name = 'categorias/detalhes.html'



@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    data = dict()
    if request.method == 'POST':
        categoria.delete()
        data['form_is_valid'] = True
        categorias = Categoria.objects.all()
        data['html_book_list'] = render_to_string('categorias/includes/lista_categoria.html', {
            'categorias': categorias
        })
    else:
        context = {'categoria': categoria}
        data['html_form'] = render_to_string('categorias/includes/excluir.html', context, request=request)
    return JsonResponse(data)

###########################Produtos############################

class Produtos( ListView):
    context_object_name = 'produtos'
    model = Produto
    template_name = 'produtos/produtos.html'
class Add_Produto(CreateView):
    form_class = ProdutoForm
    template_name = 'produtos/add_produtos.html'
    model = Produto
    success_url='/produtos'
    success_message = "produto Adicionado Com Sucesso"

class AtualizarProduto(SuccessMessageMixin,UpdateView):
    form_class = ProdutoForm
    template_name = 'produtos/add_produtos.html'
    model = Produto
    success_url='/produtos'
    success_message = "Dados Atualizados Com Sucesso"

class Produto_Detalhes(DetailView):
    model = Produto
    template_name = 'produtos/detalhes.html'


@login_required
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    data = dict()
    if request.method == 'POST':
        produto.delete()
        data['form_is_valid'] = True
        produtos = Produto.objects.all()
        data['html_book_list'] = render_to_string('produtos/includes/lista_produtos.html', {
            'produtos': produtos
        })
    else:
        context = {'produto': produto}
        data['html_form'] = render_to_string('produtos/includes/excluir.html', context, request=request)
    return JsonResponse(data)

######Entradas de produtos para o estoque#############
class Entrada(CreateView):
    form_class = EntradaForm
    template_name = 'Entradas/add_entradas.html'
    model = Entradas_Estoque
    success_url = '/produtos'



