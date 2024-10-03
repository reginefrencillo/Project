from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = 'Create periodic task for deleting expired announcements'

    def handle(self, *args, **kwargs):
        # Create or get the interval schedule
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,  # every 1 day
            period=IntervalSchedule.DAYS,
        )

        # Create the periodic task
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Delete expired announcements every day',
            task='announcement.tasks.delete_expired_announcements',
            args=json.dumps([]),  # Pass in any args if needed
        )

        self.stdout.write(self.style.SUCCESS('Periodic task created successfully.'))
