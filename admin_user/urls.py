from django.urls import path, include
from . import views
from .views import dashboard
from .views import farmer_list
from .views import employee_list
from .views import admin_employee
from .views import admin_farmer


app_name = "admin_user"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"), 
    path('admin_employee/', admin_employee, name='admin_employee'),  
    path('admin_farmer/', admin_farmer, name='admin_farmer'),  
    path('farmers/', farmer_list, name='farmer_list'),  
    path('employees/', employee_list, name='employee_list'), 

]


