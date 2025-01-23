from django.urls import path
from . import views

app_name = 'users'  # Define un namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio para usuarios (si aplica)
    path('login/', views.login_view, name='login'),  # Ruta de login
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard general
    path('musico/', views.musico_dashboard, name='musico_dashboard'),  # Dashboard para músicos
    path('oyente/', views.oyente_dashboard, name='oyente_dashboard'),  # Dashboard para oyentes
    path('productor/', views.productor_dashboard, name='productor_dashboard'),  # Dashboard para productores
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
]
