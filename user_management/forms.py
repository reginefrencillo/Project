from django import forms
from django.contrib.auth.models import User
from .models import Farmers, FarmersProfile, EmployeesProfile, Employees


class FarmerRegistrationForm(forms.ModelForm):
    farmerID = forms.IntegerField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Farmer ID'})
    )
    address = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'})
    )
    phone_number = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'})
    )
    commodities = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Commodities'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}),
        label='Confirm Password'
    )

    class Meta:
        model = Farmers
        fields = ['username', 'email', 'password', 'farmerID', 'address', 'phone_number', 'commodities']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
        }

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Farmers.base_role  # Assign the FARMER role
        user.set_password(self.cleaned_data['password'])  # Set password securely
        if commit:
            user.save()  # Save the user
            # Create the FarmersProfile with additional fields
            FarmersProfile.objects.create(
                user=user,
                farmerID=self.cleaned_data['farmerID'],
                address=self.cleaned_data.get('address'),
                phone_number=self.cleaned_data.get('phone_number'),
                commodities=self.cleaned_data.get('commodities')
            )
        return user
from django import forms
from .models import EmployeesProfile, User  # Ensure to import User model

class EmployeesRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    
    employeeID = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employee ID'}),
        label='Employee ID'
    )

    full_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'})
    )
   
    address = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'})
    )
    phone_number = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'})
    )
    commodities = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Commodities'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}),
        label='Confirm Password'
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'})
    )

    class Meta:
        model = EmployeesProfile
        fields = ['employeeID','email', 'full_name', 'password', 'address', 'phone_number', 'commodities']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if EmployeesProfile.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Create the User object
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            role=User.Role.EMPLOYEE  # Set the role of the user as EMPLOYEE
        )
        user.set_password(self.cleaned_data['password'])  # Securely set the password
        if commit:
            user.save()  # Save the user

        # Now create the EmployeesProfile
        profile = EmployeesProfile.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            address=self.cleaned_data.get('address'),
            phone_number=self.cleaned_data.get('phone_number'),
            commodities=self.cleaned_data.get('commodities')
        )
        return user

