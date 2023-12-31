from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home_app'
urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('vista/', views.PruebaListView.as_view()),
    path('prueba/', views.PruebaCreateView.as_view(), name='prueba'),
    path('foundation/', views.ResumenFoundationView.as_view(), name='foundation'),
    path('herencia/', views.HerenciaTemplate.as_view(), name='herencia'),
]