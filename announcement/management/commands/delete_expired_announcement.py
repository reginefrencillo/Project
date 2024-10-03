from django.core.management.base import BaseCommand
from announcement.models import Announcement
from django.utils import timezone  # Import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Delete announcements older than 30 days'

    def handle(self, *args, **kwargs):
        # Get the current time and calculate the cutoff time
        expired_announcements = Announcement.objects.filter(date__lt=timezone.now() - timedelta(days=2)) #sample lang sib2 days.
        count = expired_announcements.count()  # Get the number of announcements to delete
        expired_announcements.delete()  # Delete the expired announcements

        # Provide feedback in the terminal
        self.stdout.write(f'Deleted {count} expired announcements.')
