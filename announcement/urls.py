# announcement/urls.py

from django.urls import path
from . import views  # Ensure this line is present

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),  # List view at the root
    path('create/', views.create_announcement, name='create_announcement'),  # Create announcement view
]
