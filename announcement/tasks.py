# announcement/tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Announcement

@shared_task
def delete_expired_announcements():
    expired_announcements = Announcement.objects.filter(date__lt=timezone.now() - timedelta(days=30))
    count = expired_announcements.count()
    expired_announcements.delete()
    return f'Deleted {count} expired announcements.'
