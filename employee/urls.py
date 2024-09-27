from django.urls import path, include
from . import views

app_name = "employee"

urlpatterns = [
    path("employee_page/", views.employee_page, name="employee_page"),
]
