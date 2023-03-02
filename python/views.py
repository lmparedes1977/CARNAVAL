from django.shortcuts import render

from . import models


def home(req):
    """Função de renderização"""
    return render(req, 'python/paginas/home.html')


def sobre(req):
    """Função de renderização"""
    return render(req, 'python/paginas/sobre.html')


def documentacao(req):
    """Função de renderização"""
    return render(req, 'python/paginas/documentacao.html')


def exemplos(req):
    """Função de renderização"""
    aplicativos = models.Aplicativo.objects.all()
    return render(req, 'python/paginas/exemplos.html', context={'lista': aplicativos})


def exemplo(req, ap_id):
    """Função de renderização"""
    aplicativos = models.Aplicativo.objects.all()
    aplicacao = aplicativos.filter(pk=ap_id).first()
    return render(req, 'python/paginas/exemplo.html', context={'dado': aplicacao})
