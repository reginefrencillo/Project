from django.shortcuts import render


def farmer_page(request):
    return render(request, "farmers/farmer_main.html")

