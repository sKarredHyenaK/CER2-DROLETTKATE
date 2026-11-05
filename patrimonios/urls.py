from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #Vistas de autenticación de Django

app_name = 'patrimonios'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('lugar/<int:pk>/', views.detalle_lugar_view, name='detalle'), #pk dinamica
    
    #Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='patrimonios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]