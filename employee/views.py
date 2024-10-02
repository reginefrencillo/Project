from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def employee_page(request):
    return render(request, "employee/employee_main.html")
