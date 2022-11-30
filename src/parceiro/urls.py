from django.urls import path

from parceiro import views

app_name = 'parceiro'

urlpatterns = [
    path('', views.lista_parceiro, name='lista_parceiro'),
    path('cadastra_parceiro/', views.cadastra_parceiro, name='cadastra_parceiro'),
    path('exibe_parceiro/<int:id>/', views.exibe_parceiro, name='exibe_parceiro'),
    path('edita_parceiro/<int:id>/', views.edita_parceiro, name='edita_parceiro'),
    path('remove_parceiro/', views.remove_parceiro, name='remove_parceiro')
]