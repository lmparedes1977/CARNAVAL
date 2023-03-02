from django.contrib import admin

from .models import Aplicativo, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Doc"""


@admin.register(Aplicativo)
class AplicativoAdmin(admin.ModelAdmin):
    """Doc"""

    # Register your models here.
