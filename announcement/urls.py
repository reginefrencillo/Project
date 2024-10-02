from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path("announcement_list/", views.announcement_list, name="announcement_list"),
]
