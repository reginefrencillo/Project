
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from user_management.models import FarmersProfile  # Adjust import if necessary
from user_management.decorators import role_required


@login_required
@role_required(allowed_roles=['FARMER'])  # Ensure only farmers can access this view
def farmer_page(request):
    # Get the profile for the logged-in farmer
    farmer_profile = get_object_or_404(FarmersProfile, user=request.user)

    # Render the dashboard template, passing the farmer's profile data
    return render(request, 'farmers/farmer_main.html', {
        'profile': farmer_profile,
    })
