from django import forms
from .models import Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = [
            'first_name', 'middle_name', 'last_name', 'ext_name', 'house_no', 'street', 'baranggay', 'municipality', 
            'province', 'region', 'gender', 'pwd', 'contact_no', 'religion', 'educ_attainment', 'civil_status', 
            'age', 'day_of_birth', 'month_of_birth', 'year_of_birth', 'birthplace', 'name_of_spouse', 'mothers_maiden', 
            'name_of_household_head', 'relationship', 'household_members', 'household_male', 'household_female', 
            'govern_id', 'id_type', 'id_no', 'is_member', 'specify', 'if_emergency', 'emergency_contact', 
            'main_livelihood', 'position', 'specify_position'
        ]
        widgets = {
            'gender': forms.Select(choices=Farmer.GENDER_CHOICES),
            'civil_status': forms.Select(choices=Farmer.CIVIL_STATUS_CHOICES),
            'educ_attainment': forms.Select(choices=Farmer.EDUC_ATTAINMENT_CHOICES),
            'main_livelihood': forms.Select(choices=Farmer.LIVELIHOOD),
            'is_member': forms.CheckboxInput(),  # Use proper widget for Boolean fields
            'pwd': forms.CheckboxInput(),
            
        }
