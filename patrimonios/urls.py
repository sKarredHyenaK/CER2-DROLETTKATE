from django.urls import path
from . import views

app_name = 'patrimonios'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('lugar/<int:pk>/', views.detalle_lugar_view, name='detalle'), #pk dinamica
]