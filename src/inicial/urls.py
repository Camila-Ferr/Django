from django.urls import path

from inicial import views

app_name = 'inicial'

urlpatterns = [
    path('', views.index, name='inicial')
]