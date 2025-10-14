from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.models import Contato

def add_contato(request):
    if request.method != 'POST':
        return render(request, 'core/add_contato.html')
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    descricao = request.POST['descricao']
    telefone = request.POST['telefone']
    imagem = request.FILES['imagem']

    if not nome or not sobrenome:
        return render(request, 'core/add_contato.html')
    salvarContato = Contato.objects.create(nome=nome, sobrenome=sobrenome, descricao=descricao, telefone=telefone, imagem=imagem)

    salvarContato.save()
    return render(request, 'core/add_contato.html')


def listar_contato(request):
    contato = Contato.objects.all()
    return render(request, 'core/listar_contato.html',
                  {'contato': contato})





