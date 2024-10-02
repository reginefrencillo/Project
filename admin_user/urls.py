from django.urls import path, include
from . import views
from .views import farmer_list


app_name = "admin_user"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('farmers/', farmer_list, name='farmer_list'),  
]

