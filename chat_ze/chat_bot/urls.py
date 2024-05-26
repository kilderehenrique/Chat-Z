from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    
    path('resumo', view=views.resumo, name="resumo"),
    path('resumo/', RedirectView.as_view(url="../resumo")),

    path('traducao', view=views.traducao, name="traducao"),
    path('traducao/', RedirectView.as_view(url="../traducao")),
    
    path('gerar_codigo', view=views.gerar_codigo, name="gerar_codigo"),
    path('gerar_codigo/', RedirectView.as_view(url="../gerar_codigo")),
]
