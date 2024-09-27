from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "admin_user/admin_main.html")

