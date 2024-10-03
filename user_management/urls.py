from django.urls import path
from . import views
from .views import registerEmployee  # Import the view here


urlpatterns = [
    path('registerFarmer/', views.registerFarmer, name='registerFarmer'),  
    path('registerEmployee/', registerEmployee, name='registerEmployee'),  # Adjust path as needed
    path('login/', views.login, name="login"),
]
