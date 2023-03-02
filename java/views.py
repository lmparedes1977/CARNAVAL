from django.shortcuts import render

from . import models

# from utils.aplicacoes import fabrica


# lista_aplicacoes = [fabrica.cria_aplicacao() for _ in range(10)]


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
    aplicativos = models.Aplicativo.objects.all()
    return render(req, 'java/paginas/exemplos.html', context={'lista': aplicativos})


def exemplo(req, ap_id):
    """Função de renderização"""
    # for app in aplicativos:
    #     if app['titulo'] == id:
    #         aplicacao = app
    aplicativos = models.Aplicativo.objects.all()
    aplicacao = aplicativos.filter(pk=ap_id).first()
    return render(req, 'java/paginas/exemplo.html', context={'dado': aplicacao})


def bootstrap(req):
    """Função de renderização"""
    return render(req, 'java/paginas/modelo.html')
