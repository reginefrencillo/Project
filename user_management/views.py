# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FarmerRegistrationForm
from .forms import EmployeesRegistrationForm
# users/views.py
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def registerFarmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            new_farmer = form.save()
            messages.success(request, 'Farmer added successfully!')
            return redirect('user_management:registerFarmer')  # Adjust redirect as needed
        else:
            print(form.errors)  # Log errors for debugging
            messages.error(request, 'Failed to add the farmer. Please check the details and try again.')
    else:
        form = FarmerRegistrationForm()

    return render(request, 'user_management/register_farmer.html', {'form': form})



def registerEmployee(request):
    if request.method == 'POST':
        form = EmployeesRegistrationForm(request.POST)
        if form.is_valid():
            new_employee = form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('user_management:registerEmployee')  # Adjust to your actual employee list view
        else:
            logger.error(form.errors)  # Log errors for debugging
            messages.error(request, 'Failed to add the employee. Please check the details and try again.')
    else:
        form = EmployeesRegistrationForm() 
    return render(request, 'user_management/register_employee.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Log in the user
            # Debug: Print user role to console
            print(f"User {user.username} has role {user.role}")
            
            # Redirect based on user role
            if user.role == 'ADMIN':
                return redirect('admin_user:dashboard')  # Redirect to admin dashboard
            elif user.role == 'EMPLOYEE':
                return redirect('employee:employee_page')  # Redirect to employee dashboard
            elif user.role == 'FARMER':
                return redirect('farmers:farmer_page')  # Redirect to farmer dashboard
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'user_management/login.html')  # Adjust template path
