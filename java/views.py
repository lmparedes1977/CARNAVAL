from django.shortcuts import render
from utils.aplicacoes import fabrica

lista_aplicacoes = [fabrica.cria_aplicacao() for _ in range(10)]

def home(req):
    """Função de renderização"""
    return render(req, 'java/paginas/home.html')

def sobre(req):
    """Função de renderização"""
    return render(req, 'java/paginas/sobre.html')

def documentacao(req):
    """Função de renderização"""
    return render(req, 'java/paginas/documentacao.html')

def exemplos(req):
    """Função de renderização"""
    return render(req, 'java/paginas/exemplos.html', context={'lista': lista_aplicacoes})

def exemplo(req, id):
    """Função de renderização"""
    for app in lista_aplicacoes:
        if app['titulo'] == id:
            aplicacao = app
    return render(req, 'java/paginas/exemplo.html', context={'id': aplicacao})

def bootstrap(req):
    """Função de renderização"""
    return render(req, 'java/paginas/modelo.html')
