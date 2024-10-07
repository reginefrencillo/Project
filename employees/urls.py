from django.urls import path, include
from . import views

app_name = 'employee'

urlpatterns = [
    #sidebar links
    path('employee_page/', views.employee_page, name='employee_page'),
    path('insurance_application/', views.insurance_application, name='insurance_application'),
    path('reports/', views.reports, name='reports'),


    path('farmers_commodity/', views.farmers_commodity, name='farmers_commodity'),
    path('farmer_profile/', views.farmer_profile, name='farmer_profile'),
    path('farmer_create/', views.farmer_create, name='farmer_create'),
    path('farmer_update/<int:pk>/farmer_update,', views.farmer_update, name='farmer_update'),
    path('farmer_delete/<int:pk>/farmer_delete/', views.farmer_delete, name='farmer_delete'),
]
