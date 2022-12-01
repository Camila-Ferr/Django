from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', include('inicial.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('ranking/', include('ranking.urls')),
    path('parceiro/',include('parceiro.urls')),
    path('metas/', include('metas.urls')),
    path('produto/', include('produto.urls'))
]

#     Como acessar a página produto.html do projeto:
#     http://127.0.0.1:8000/
#
#     Como acessar a página produto.html de inicial:
#     http://127.0.0.1:8000/inicial/