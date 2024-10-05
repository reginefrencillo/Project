from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_management.decorators import role_required

from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer
from .forms import FarmerForm


#sidebar link
app_name = 'employee'
@login_required
@role_required(allowed_roles=['EMPLOYEE'])
def employee_page(request):
    return render(request, "employee/employee_main.html")

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
def employee_insurance_application(request):
    return render(request, "employee/employee_insurance_app.html")

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
def employee_reports(request):
    return render(request, "employee/employee_reports.html")



@login_required
@role_required(allowed_roles=['EMPLOYEE'])
def farmers_list(request):
    return render(request, 'employee/barangay_to_farmer_list.html')

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
# Create a new Farmer
def farmer_create(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee:farmer_profile')
        else:
            print(form.errors)
    else:
        form = FarmerForm()
    return render(request, 'employee/add_farmer_profile.html', {'form': form})

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
# List all Farmers
def farmer_profile(request):
    farmers = Farmer.objects.all()
    return render(request, 'employee/view_farmer_profile.html', {'farmers': farmers})

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
# Update an existing Farmer
def farmer_update(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('employee:farmer_profile')
    else:
        form = FarmerForm(instance=farmer)
    return render(request, 'employee/add_farmer.html', {'form': form})

@login_required
@role_required(allowed_roles=['EMPLOYEE'])
# Delete a Farmer
def farmer_delete(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('employee:farmer_profile')
    return render(request, 'employee/farmer_confirm_delete.html', {'farmer': farmer})