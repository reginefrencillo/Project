from django.urls import path, include
from . import views

app_name = "admin_user"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
