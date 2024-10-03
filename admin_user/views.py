from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_management.models import User
from user_management.models import FarmersProfile
from user_management.models import EmployeesProfile  # Import your EmployeesProfile model


# Create your views here.
def dashboard(request):
    return render(request, "admin_user/admin_main.html")

def farmer_list(request):
    farmers = FarmersProfile.objects.select_related('user').all()  # Fetch all farmers and their profiles
    return render(request, 'admin_user/farmer_list.html', {'farmers': farmers})


def employee_list(request):
    # Use select_related to fetch related User data efficiently
    employees = EmployeesProfile.objects.select_related('user').all()  # Fetch all employees and their profiles
    return render(request, 'admin_user/employee_list.html', {'employees': employees})

def admin_employee(request):
    return render(request, "admin_user/admin_employee.html")

def admin_farmer(request):
    return render(request, "admin_user/admin_farmer.html")