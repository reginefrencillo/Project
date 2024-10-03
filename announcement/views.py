from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib import messages
from django.utils import timezone  # Import timezone


# Create your views here.
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(
        request, "announcement/announcement_list.html", {"announcements": announcements}
    )




def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Announcement created successfully!')
            return redirect('announcement_create')  # Redirect back to the create announcement page
        else:
            messages.error(request, 'Failed to create the announcement. Please ensure all fields are filled correctly.')
    else:
        form = AnnouncementForm()

    return render(request, 'announcement/create_ann.html', {'form': form})
