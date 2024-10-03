from django.db import models
from django.utils import timezone
from datetime import timedelta

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_expired(self):
        return timezone.now() > self.date + timedelta(days=30)
