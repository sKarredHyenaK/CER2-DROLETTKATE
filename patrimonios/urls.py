from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #Vistas de autenticación de Django

app_name = 'patrimonios'    #indicar a qué aplicación pertenece la ruta

urlpatterns = [
    path('', views.index_view, name='index'),       #pagina de inicio
    path('catalogo/', views.catalogo_view, name='catalogo'),        #catalogo
    path('lugar/<int:pk>/', views.detalle_lugar_view, name='detalle'), #<int:pk> -> ID del monumento y conforme a eso muestra detalle
    
    #Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='patrimonios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]