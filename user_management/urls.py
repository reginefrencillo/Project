from django.urls import path
from . import views
from .views import registerEmployee  # Import the view here


app_name = 'user_management'

urlpatterns = [
    path('registerFarmer/', views.registerFarmer, name='registerFarmer'),  
    path('registerEmployee/', registerEmployee, name='registerEmployee'),  # Adjust path as needed
    path('login/', views.login, name="login"),
    path('logoutUser/', views.logoutUser, name='logoutUser')
]
