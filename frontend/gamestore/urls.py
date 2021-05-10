from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='gamestore-login'),
    path('home/', views.home, name='gamestore-home'),
    path('about/', views.about, name='gamestore-about'),
    path('registro/', views.registro, name='gamestore-registro'),
    path('signup/',views.signup, name='signup'),
    path('recibirTexto/',views.RecibirTexto, name='recibirTexto'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.login, name='login'),
    path('graficar/', views.graficar, name='graficar'),
    path('cargarGraficar/', views.cargarGrafica, name='cargarGrafica'),
    path('graficar2/', views.graficar2, name='graficar2'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('ayuda1/', views.ayuda1, name='ayuda1'),
    path('reset/', views.reset, name='reset'),
    
]