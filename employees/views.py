from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer
from .forms import FarmerForm
from django.contrib.auth.decorators import login_required
from user_management.decorators import role_required

# Create your views here.

app_name = 'employee'

#sidebar links
@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def employee_page(request):
    return render(request, 'employees/employee_main.html')


@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def insurance_application(request):
    return render(request, 'employees/employee_insurance_app.html')

@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def reports(request):
    return render(request, 'employees/employee_reports.html')




@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def farmers_commodity(request):
    return render(request, 'employees/farmers_commodity.html')

# Create a new Farmer
@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def farmer_create(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:farmer_profile')
        else:
            print(form.errors)
    else:
        form = FarmerForm()
    return render(request, 'employees/add_farmer.html', {'form': form})

# List all Farmers
@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def farmer_profile(request):
    farmers = Farmer.objects.all()
    return render(request, 'employees/view_farmer_profile.html', {'farmers': farmers})

# Update an existing Farmer
@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def farmer_update(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('employees:farmer_profile')
    else:
        form = FarmerForm(instance=farmer)
    return render(request, 'employees/add_farmer.html', {'form': form})

# Delete a Farmer
@login_required
@role_required(allowed_roles=['EMPLOYEE'])  
def farmer_delete(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('employees:farmer_profile')
    return render(request, 'employees/farmer_confirm_delete.html', {'farmer': farmer})