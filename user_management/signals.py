# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FarmersProfile, Farmers

@receiver(post_save, sender=Farmers)
def create_or_update_user_profile(sender, instance, **kwargs):
    FarmersProfile.objects.update_or_create(user=instance, defaults={
        'farmerID': instance.farmerID,
        'commodities': instance.commodities,
        'address': instance.address,
        'phone_number': instance.phone_number,
    })
