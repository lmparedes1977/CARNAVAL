from django.shortcuts import render
from utils.aplicacoes import fabrica

lista_aplicacoes = [fabrica.cria_aplicacao() for _ in range(10)]

def home(req):
    """Função de renderização"""
    return render(req, 'jscript/paginas/home.html')

def sobre(req):
    """Função de renderização"""
    return render(req, 'jscript/paginas/sobre.html')

def documentacao(req):
    """Função de renderização"""
    return render(req, 'jscript/paginas/documentacao.html')

def exemplos(req):
    """Função de renderização"""
    return render(req, 'jscript/paginas/exemplos.html', context={'lista': lista_aplicacoes})

def exemplo(req, id):
    """Função de renderização"""
    for app in lista_aplicacoes:
        if app['titulo'] == id:
            aplicacao = app
    return render(req, 'jscript/paginas/exemplo.html', context={'id': aplicacao})
