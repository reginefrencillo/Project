from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def farmer_page(request):
    return render(request, "farmers/farmer_main.html")
