from django.contrib import admin 
from django.urls import path, include 
from inventario import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
# Sistema de Autenticación integrado 
    path('accounts/', include('django.contrib.auth.urls')),  
# Rutas de la App 
    path('', views.lista_productos, name='lista_productos'), 
    path('nuevo/', views.crear_producto, name='crear_producto'), 
]