from django.urls import path

from metas import views

app_name = 'metas'

urlpatterns = [
    path('', views.meta, name='index')
]