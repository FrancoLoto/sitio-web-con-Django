from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('registro/', views.register_page, name="register"),
    path('ingreso/', views.login_page, name="login"),
    path('salir/', views.logout_user, name="logout"),
]