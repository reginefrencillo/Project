from django.urls import path
from . import views

urlpatterns = [
    path('registerFarmer/', views.registerFarmer, name='registerFarmer'),  
    path('login/', views.login, name="login"),
]
