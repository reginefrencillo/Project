from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FarmerRegistrationForm, EmployeesRegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .decorators import role_required
import logging

# Configure logger
logger = logging.getLogger(__name__)

@login_required
@role_required(allowed_roles=['ADMIN'])  # Only admins can register farmers
def registerFarmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            new_farmer = form.save()
            messages.success(request, 'Farmer added successfully!')
            return redirect('user_management:registerFarmer')
        else:
            logger.error(form.errors)
            messages.error(request, 'Failed to add the farmer. Please check the details and try again.')
    else:
        form = FarmerRegistrationForm()

    return render(request, 'user_management/register_farmer.html', {'form': form})


@login_required
@role_required(allowed_roles=['ADMIN'])  # Only admins can register employees
def registerEmployee(request):
    if request.method == 'POST':
        form = EmployeesRegistrationForm(request.POST)
        if form.is_valid():
            new_employee = form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('user_management:registerEmployee')
        else:
            logger.error(form.errors)
            messages.error(request, 'Failed to add the employee. Please check the details and try again.')
    else:
        form = EmployeesRegistrationForm()
    return render(request, 'user_management/register_employee.html', {'form': form})


@csrf_exempt  # Optional: Only if you really need it; consider removing it if not needed
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            print(f"User {user.username} has role {user.role}")
            
            if user.role == 'ADMIN':
                return redirect('admin_user:dashboard')
            elif user.role == 'EMPLOYEE':
                return redirect('employee:employee_page')
            elif user.role == 'FARMER':
                return redirect('farmers:farmer_page')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('user_management:login')

    return render(request, 'user_management/login.html')


def logoutUser(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    return redirect('user_management:login')
