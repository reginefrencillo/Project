from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_management.models import User
from user_management.models import FarmersProfile



# Create your views here.
def dashboard(request):
    return render(request, "admin_user/admin_main.html")

def farmer_list(request):


    farmers = FarmersProfile.objects.select_related('user').all()  # Fetch all farmers and their profiles
    return render(request, 'admin_user/farmer_list.html', {'farmers': farmers})
