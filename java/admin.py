from django.contrib import admin

from .models import Aplicativo, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    """Doc"""


class AplicativoAdmin(admin.ModelAdmin):
    """Doc"""


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Aplicativo, AplicativoAdmin)


# método alternativo para registro das clases/tabelas:
# @admin.register(Categoria)
# Class CategoriaAdmin(admin.modelAdmin):

# @admin.register(Aplicativo)
# Class AplicativoAdmin(admin.modelAdmin):
