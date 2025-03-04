from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.auth.models import User

class Register(AbstractUser):
    usertype=models.CharField(max_length=50,default="admin")
    contact=models.IntegerField(null=True)
    image=models.ImageField(upload_to='uploads/',null=True)
    licence_no=models.CharField(max_length=60,null=True)
    is_approved=models.BooleanField(default=True)


class Reset(models.Model):
    otp = models.CharField(max_length=6, null=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True,related_name='otp')
    otp_created_at = models.DateTimeField(auto_now_add =True)
class Policy(models.Model):
    provider_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    details = models.TextField()
    cover_amount = models.CharField(max_length=255)  # Add cover_amount field
    no_months=models.CharField(max_length=255)
    total_amnt= models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) # Use settings.AUTH_USER_MODEL
    created_on = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='policy_images/', null=True, blank=True)  # Add this line
    

    def __str__(self):
        return self.name
class UserMedicalInfo(models.Model):
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE, related_name='medical_info')
    name = models.CharField(max_length=255)
    address = models.TextField()
    pincode = models.CharField(max_length=6)  # Or IntegerField if you prefer
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)  # Or use PhoneNumberField if you have a library for that
    email = models.EmailField()
    medical_condition = models.TextField(blank=True, null=True)
    health_reports = models.FileField(upload_to='health_reports/', blank=True, null=True)

    def __str__(self):
        return self.name





