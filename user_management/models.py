from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EMPLOYEE = "EMPLOYEE", "Employee"
        FARMER = "FARMER", "Farmer"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)



User = get_user_model()

class FarmerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.FARMER)

class Farmers(User): 
    base_role = User.Role.FARMER

    class Meta:
        proxy = True

    farmers = FarmerManager()

    def welcome(self):
        return "Welcome, Farmer!"

@receiver(post_save, sender=Farmers)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "FARMER":
        FarmersProfile.objects.create(user=instance)

class FarmersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farmerID = models.IntegerField(null=True, blank=True)
    commodities = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)  # Example of a custom field
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Example of another custom field



# shows query set of all Employees, Employees.all()
class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EMPLOYEE)


class Employees(User):
    base_role = User.Role.EMPLOYEE

    class Meta:
        proxy = True

    employees = EmployeeManager()

    def welcome(self):
        return "Welcome, EMPLOYEE!"
