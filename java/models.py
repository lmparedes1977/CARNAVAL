# from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    """Doc"""
    nome = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f'{self.nome}'


class Aplicativo(models.Model):
    """Doc"""
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    slug = models.SlugField()  # urls
    ano_lancamento = models.IntegerField()
    nr_usuarios = models.IntegerField()
    foto = models.ImageField(upload_to='imagens/%Y/%m/%d/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.nome}'
