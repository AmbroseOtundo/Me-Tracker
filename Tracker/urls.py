from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('login/', views.loginuser, name='loginuser'),
    path('register/', views.register_request, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/my_dosage_list/', views.my_dosage_list, name="dosagelist"),
    
    path("logout", views.logout_request, name= "logout"),

]
