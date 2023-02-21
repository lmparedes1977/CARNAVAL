from django.urls import path
from . import views

app_name = 'java'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('documentacao/', views.documentacao, name='documentacao'),
    path('exemplos/', views.exemplos, name='exemplos'),
    path('exemplos/exemplo/<str:id>', views.exemplo, name='exemplo'),
    path('bootstrap/', views.bootstrap, name='bootstrap')
]
