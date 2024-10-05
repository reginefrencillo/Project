from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_management.decorators import role_required

@login_required
@role_required(allowed_roles=['FARMER'])
def farmer_page(request):
    return render(request, "farmers/farmer_main.html")
