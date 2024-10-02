from django import forms
from django.contrib.auth.models import User
from .models import Farmers, FarmersProfile
from django import forms
from .models import Farmers, FarmersProfile

class FarmerRegistrationForm(forms.ModelForm):
    farmerID = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Farmer ID'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    commodities = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Commodities'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}), label='Confirm Password')

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
