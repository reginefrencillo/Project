from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_management.models import User
from user_management.models import FarmersProfile
from user_management.models import EmployeesProfile  # Import your EmployeesProfile model
from django.contrib.auth.decorators import login_required
from user_management.decorators import role_required

@login_required
@role_required(allowed_roles=['ADMIN'])
def dashboard(request):
    return render(request, "admin_user/admin_main.html")

@login_required
@role_required(allowed_roles=['ADMIN'])
def farmer_list(request):
    farmers = FarmersProfile.objects.select_related('user').all()  # Fetch all farmers and their profiles
    return render(request, 'admin_user/farmer_list.html', {'farmers': farmers})

@login_required
@role_required(allowed_roles=['ADMIN'])
def employee_list(request):
    # Use select_related to fetch related User data efficiently
    employees = EmployeesProfile.objects.select_related('user').all()  # Fetch all employees and their profiles
    return render(request, 'admin_user/employee_list.html', {'employees': employees})

@login_required
@role_required(allowed_roles=['ADMIN'])
def admin_employee(request):
    return render(request, "admin_user/admin_employee.html")

@login_required
@role_required(allowed_roles=['ADMIN'])
def admin_farmer(request):
    return render(request, "admin_user/admin_farmer.html")