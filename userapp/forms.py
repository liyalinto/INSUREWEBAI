from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
# from django.core.validators import RegexValidator
from .models import UserMedicalInfo

class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(
        max_length=20,
        label="CONFIRM PASSWORD",
        required=True,
        widget=forms.PasswordInput(attrs={'id':'confirm_password','name':'confirm_password'})
    )
    class Meta:
        model=Register
        fields=['first_name','last_name','username','email','contact','password']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
            
        }
        labels={
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'password':'PASSWORD'
        }
        help_texts={
            'username':None
        }
   
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact
    
    # Custom Validation for password
    def clean_password(self):
        password = self.cleaned_data.get('password')
         # Only validate if password is required
        if self.fields['password'].required:
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            if not re.search(r'\d', password):
                raise ValidationError("Password must contain at least one digit.")
            if not re.search(r'[A-Za-z]', password):
                raise ValidationError("Password must contain at least one letter.")
        return password
        
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password


    

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label="USERNAME",
        widget=forms.TextInput(attrs={'id':'username','name':'username'})
    )
    password=forms.CharField(
        max_length=20,
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'})
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['first_name', 'last_name', 'username', 'email', 'contact','image']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'last_name':forms.TextInput(attrs={'id':'last_name','name':'last_name'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image',}),
            
        }
        labels={
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'image':'IMAGE'
        }
        help_texts={
            'username':None
        }
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("This username is already taken.")

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact







class staff_registerForm(forms.ModelForm):
    confirm_password=forms.CharField(
        max_length=20,
        label="CONFIRM PASSWORD",
        required=True,
        widget=forms.PasswordInput(attrs={'id':'confirm_password','name':'confirm_password'})
    )
    class Meta:
        model=Register
        fields=['first_name','last_name','username','email','contact','password']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image',})
            
        }
        labels={
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'password':'PASSWORD',
            'image':'IMAGE'
        }
        help_texts={
            'username':None
        }
   
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact
    
    # Custom Validation for password
    def clean_password(self):
        password = self.cleaned_data.get('password')
         # Only validate if password is required
        if self.fields['password'].required:
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            if not re.search(r'\d', password):
                raise ValidationError("Password must contain at least one digit.")
            if not re.search(r'[A-Za-z]', password):
                raise ValidationError("Password must contain at least one letter.")
        return password
        
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password


    

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label="USERNAME",
        widget=forms.TextInput(attrs={'id':'username','name':'username'})
    )
    password=forms.CharField(
        max_length=20,
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'})
    )

class StaffEditProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['first_name', 'last_name', 'username', 'email', 'contact','image']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'last_name':forms.TextInput(attrs={'id':'last_name','name':'last_name'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image',}),
            
        }
        labels={
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'image':'IMAGE'
        }
        help_texts={
            'username':None
        }
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("This username is already taken.")

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact






















    
class hospital_RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(
        max_length=20,
        label="CONFIRM PASSWORD",
        required=True,
        widget=forms.PasswordInput(attrs={'id':'confirm_password','name':'confirm_password'})
    )
    class Meta:
        model=Register
        fields=['first_name','username','email','contact','password','licence_no']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
            'licence_no':forms.TextInput(attrs={'id':'licence_no','name':'licence_no'}),
        }
        labels={
            'first_name':'HOSPITAL NAME',
           
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'password':'PASSWORD',
            'licence_no':'LICENCE NUMBER',
        }
        help_texts={
            'username':None
        }
   
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact
    
    # Custom Validation for password
    def clean_password(self):
        password = self.cleaned_data.get('password')
         # Only validate if password is required
        if self.fields['password'].required:
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            if not re.search(r'\d', password):
                raise ValidationError("Password must contain at least one digit.")
            if not re.search(r'[A-Za-z]', password):
                raise ValidationError("Password must contain at least one letter.")
        return password
        
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password


    

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label="USERNAME",
        widget=forms.TextInput(attrs={'id':'username','name':'username'})
    )
    password=forms.CharField(
        max_length=20,
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'})
    )

class HospitalEditProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['first_name','username', 'email', 'contact','image','licence_no']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'contact':forms.TextInput(attrs={'id':'contact','name':'contact'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image',}),
            'licence_no':forms.TextInput(attrs={'id':'licence_no','name':'licence_no'}),
            
        }
        labels={
            'first_name':'FIRST NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'contact':'CONTACT NUMBER',
            'image':'IMAGE',
            'licence_no':'LICENCE NUMBER',
        }
        help_texts={
            'username':None
        }
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("This username is already taken.")

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_contact(self):
        contact = str(self.cleaned_data.get('contact'))  # Ensure contact is a string
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return contact
    
class ForgotPasswordForm(forms.Form):
    email = forms.CharField(max_length = 50, label="Email", widget = forms.EmailInput(attrs = {'name':'email','id':'email'}))


class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length = 6, label="otp", widget = forms.TextInput(attrs = {'name':'otp','id':'otp'}))
    email = forms.CharField(max_length = 50, label="Email", widget = forms.EmailInput(attrs = {'name':'email','id':'email'}))
    new_password = forms.CharField(max_length = 50, label="New password", widget = forms.PasswordInput(attrs = {'name':'new_password','id':'new_password'}))
    confirm_password = forms.CharField(max_length = 50, label="confirm new password", widget = forms.PasswordInput(attrs = {'name':'confirm_password','id':'confirm_password'}))
    

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['provider_name','name', 'details','cover_amount','no_months','total_amnt','image']  # Fields to include in the form
        #You can customize the form widgets here if needed, like:
        #widgets = {'details': forms.Textarea(attrs={'rows': 5})}






class UserMedicalInfoForm(forms.ModelForm):
    class Meta:
        model = UserMedicalInfo
        fields = [
            'name', 'address', 'pincode', 'age', 'phone_number', 'email', 
            'medical_condition', 'health_reports'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),  # Adjust rows as needed
            'medical_condition': forms.Textarea(attrs={'rows': 5}), # Adjust rows as needed
        }
#If you want to use widgets to customize the form field.
# class UserMedicalInfoForm(forms.ModelForm):
#     class Meta:
#         model = UserMedicalInfo
#         fields = ['name', 'other_details', 'medical_condition', 'health_reports']  # Include all fields
#         widgets = {
#             'medical_condition': forms.Textarea(attrs={'rows': 5}), # example to change the medical_condition field to a text area with 5 rows.
#         }
