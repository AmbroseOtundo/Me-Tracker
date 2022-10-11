from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register_request, name='register'),
    path('homepage/', views.homepage, name='homepage')
]
