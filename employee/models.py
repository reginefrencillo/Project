from django.db import models

class Farmer(models.Model):
    # Dropdown options for gender, civil status, educ attainment, and religion
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CIVIL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]

    EDUC_ATTAINMENT_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('G', 'Graduate'),
    ]

    LIVELIHOOD = [
        ('Farmer', 'Farmer'),
        ('Farmworkers', 'Farmworkers'),
        ('Fisherfolk', 'Fisherfolk')
    ]

    # Personal Information Fields
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    ext_name = models.CharField(max_length=10, blank=True, null=True)
    
    # Address Fields
    house_no = models.CharField(max_length=10, default="", null=False)
    street = models.CharField(max_length=100, default="", null=False)
    baranggay = models.CharField(max_length=100, default="", null=False)
    municipality = models.CharField(max_length=100, default="", null=False)
    province = models.CharField(max_length=100, default="", null=False)
    region = models.CharField(max_length=100, default="", null=False)
    
    # Other Information
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    pwd = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=15)
    
    religion = models.CharField(max_length=10, default="", null=False)
    educ_attainment = models.CharField(max_length=10, choices=EDUC_ATTAINMENT_CHOICES, default='HS')
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS_CHOICES, default='S')
    
    # Birth Information
    age = models.IntegerField(null=True, blank=True)
    day_of_birth = models.IntegerField(default=1, null=False)
    month_of_birth = models.IntegerField(default=1, null=False)
    year_of_birth = models.IntegerField(default=2000, null=False)
    birthplace = models.CharField(max_length=100, default="", null=False)
    
    # Family Information
    name_of_spouse = models.CharField(max_length=100, blank=True, null=True)
    mothers_maiden = models.CharField(max_length=100, blank=True, null=True)
    name_of_household_head = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)
    
    # Household Information
    household_members = models.IntegerField(null=True, blank=True)
    household_male = models.IntegerField(null=True, blank=True)
    household_female = models.IntegerField(null=True, blank=True)
    
    # Government ID Information
    govern_id = models.CharField(max_length=100, blank=True, null=True)
    id_type = models.CharField(max_length=50, blank=True, null=True)
    id_no = models.CharField(max_length=100, blank=True, null=True)
    
    # Membership Information
    is_member = models.BooleanField(default=False)
    specify = models.CharField(max_length=100, blank=True, null=True)
    
    # Emergency Information
    if_emergency = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    
    # Livelihood Information
    main_livelihood = models.CharField(max_length=20, choices=LIVELIHOOD, default='Farmer')
    position = models.CharField(max_length=100, blank=True, null=True)
    specify_position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
