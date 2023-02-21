from django.shortcuts import render

# Create your views here.


def home(req):
    """Função de renderização"""
    return render(req, 'home/paginas/home.html')

def sobre(req):
    """Função de renderização"""
    return render(req, 'home/paginas/sobre.html')

def contato(req):
    """Função de renderização"""
    return render(req, 'home/paginas/contato.html')

def bootstrap(req):
    """Função de renderização"""
    return render(req, 'home/paginas/modelo.html')
