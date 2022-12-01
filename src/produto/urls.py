from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.produto, name='index'),
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('atualiza_produtos/', views.atualiza_produtos, name='atualiza_produtos'),
]