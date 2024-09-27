from django.urls import path, include
from . import views

app_name = "farmers"

urlpatterns = [
    path("farmer_page/", views.farmer_page, name="farmer_page"),
]
