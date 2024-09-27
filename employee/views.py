from django.shortcuts import render

# Create your views here.
def employee_page(request):
    return render(request, "employee/employee_main.html")

