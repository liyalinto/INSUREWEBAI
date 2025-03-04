from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail
import string, secrets
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from django.contrib import messages

# Create your views here.
def index(request):
    policies = Policy.objects.all() 
    return render(request,'index.html',{'policies':policies})


def about(request):
    return render(request,'about.html')
def insurance(request):
    return render(request,'insurance.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                users=Register.objects.get(username=user)
                request.session['ut']=users.usertype
                request.session['uid']=users.id
                request.session['uname']=users.username
                messages.success(request,"login succesfull",extra_tags="success")
                return redirect('/')
            else:
                messages.error(request,"invalid username and password",extra_tags="error")
        else:
            messages.error(request,"login failed",extra_tags="error")
            print(form.errors)
            form=LoginForm()
            return render(request,'login.html',{'form':form})
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        print("---------------------------")
        form=RegisterForm(request.POST)
        if form.is_valid():
            print("===================================")
            # checking the email exists or not
            email = form.cleaned_data['email']
            data = Register.objects.filter(email=email)
            if data:
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="user"
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            form=RegisterForm()
            return render(request,'register.html',{'form':form,'title':'Register'})
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form,'title':'Register'})

def user_logout(request):
    logout(request)
    messages.success(request,"logout sucesssfully",extra_tags="success")
    return redirect('/')


def view_user(request):
    users=Register.objects.filter(usertype="user")
    return render(request,'users.html',{'users':users})
def approve_user(request,id):
    user=Register.objects.get(id=id)
    user.is_approved=True
    user.save()
    messages.success(request,'user approved successfully',extra_tags="success")
    return redirect('view_user')


def reject_user(request,id):
    user=Register.objects.get(id=id)
    subject="Account Rejection Notification"
    message=f"Dear {user.username} Your registration is being Rejected. Please register again with valid details for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'user rejected successfully',extra_tags='success')
    return redirect('view_user')





def view_staff(request):
    staffs=Register.objects.filter(usertype="staff")
    return render(request,'view_staff.html',{'staffs':staffs})
def view_hospital(request):
    hospitals=Register.objects.filter(usertype="hospital")
    return render(request,'view_hospital.html',{'hospitals':hospitals})

def approve_hospital(request,id):
    hospital=Register.objects.get(id=id)
    hospital.is_approved=True
    hospital.save()
    messages.success(request,'hospital approved successfully',extra_tags="success")
    return redirect('view_hospital')


def reject_hospital(request,id):
    hospital=Register.objects.get(id=id)
    subject="Account Rejection Notification"
    message=f"Dear {hospital.username} Your registration is being Rejected. Please register again with valid details for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[hospital.email]
    send_mail(subject, message, email_from, email_to)

    hospital.delete()
    messages.success(request,'hospital rejected successfully',extra_tags='success')
    return redirect('view_hospital')






def profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request,'profile.html',{'user':user})

def staff_profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request,'staff_profile.html',{'user':user})
def hospital_profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request,'staff_profile.html',{'user':user})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'register.html', {'form': form,'title':'update'})

def delete_user(request,id):
    user=Register.objects.get(id=id)

    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'user deleted successfully',extra_tags='success')
    return redirect('view_user')

def delete_staff(request,id):
    user=Register.objects.get(id=id)

    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'staff deleted successfully',extra_tags='success')
    return redirect('view_staff')
def delete_hospital(request,id):
    user=Register.objects.get(id=id)

    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'hospital deleted successfully',extra_tags='success')
    return redirect('view_hospital')
def approve_staff(request,id):
    staff=Register.objects.get(id=id)
    staff.is_approved=True
    staff.save()
    messages.success(request,'staff approved successfully',extra_tags="success")
    return redirect('view_staff')


def reject_staff(request,id):
    staff=Register.objects.get(id=id)
    subject="Account Rejection Notification"
    message=f"Dear {staff.username} Your registration is being Rejected. Please register again with valid details for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[staff.email]
    send_mail(subject, message, email_from, email_to)

    staff.delete()
    messages.success(request,'staff rejected successfully',extra_tags='success')
    return redirect('view_staff')



def staffregister(request):
    if request.method == 'POST':
        print("---------------------------")
        form=staff_registerForm(request.POST)
        if form.is_valid():
            print("===================================")
            # checking the email exists or not
            email = form.cleaned_data['email']
            data = Register.objects.filter(email=email)
            if data:
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="staff"
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            form=staff_registerForm()
            return render(request,'register.html',{'form':form,'title':'Register'})
    else:
        form=staff_registerForm()
    return render(request,'register.html',{'form':form,'title':'Register'})

def user_logout(request):
    logout(request)
    messages.success(request,"logout sucesssfully",extra_tags="success")
    return redirect('/')

def view_user(request):
    users=Register.objects.filter(usertype="user")
    return render(request,'users.html',{'users':users})

def profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request,'profile.html',{'user':user})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'register.html', {'form': form,'title':'update'})

def delete_user(request,id):
    user=Register.objects.get(id=id)

    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'user deleted successfully',extra_tags='success')
    return redirect('view_user')


def staff_edit_profile(request):
    if request.method == 'POST':
        form = StaffEditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = StaffEditProfileForm(instance=request.user)

    return render(request, 'register.html', {'form': form,'title':'update'})
















def hospital_register(request):
    if request.method == 'POST':
        print("---------------------------")
        form=hospital_RegisterForm(request.POST)
        if form.is_valid():
            print("===================================")
            # checking the email exists or not
            email = form.cleaned_data['email']
            data = Register.objects.filter(email=email)
            if data:
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="hospital"
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            form=hospital_RegisterForm()
            return render(request,'register.html',{'form':form,'title':'Register'})
    else:
        form=hospital_RegisterForm()
    return render(request,'register.html',{'form':form,'title':'Register'})
def registerationtype(request):
    return render(request,'registerationtype.html')


def hospital_edit_profile(request):
    if request.method == 'POST':
        form = HospitalEditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = HospitalEditProfileForm(instance=request.user)

    return render(request, 'register.html', {'form': form,'title':'update'})


def forgot_password(request):
        if request.method =='POST':
            form=ForgotPasswordForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                data = Register.objects.filter(email=email)
                if data:
                    new_password=generate_random_password()
                    user=Register.objects.get(email=email)
                    Reset.objects.create(otp=new_password,user=user)
                    subject="Reset password"
                    message=f"your one time password is {new_password}"
                    email_from=settings.EMAIL_HOST_USER
                    email_to=[email]
                    send_mail(subject, message, email_from, email_to)
                    messages.success(request,'OTP successfully sent',extra_tags='success')
                    return redirect('reset_password')
                else:
                    messages.error(request,'email does not exist',extra_tags='error')
            else:
                messages.error(request,'invalid form data')
        else:
            form=ForgotPasswordForm()
        return render(request,'forgot_password.html',{'form':form})

def generate_random_password(length=6):
    characters=string.ascii_letters+string.digits
    password=''.join(secrets.choice(characters) for _ in range(length))
    return password

def reset_password(request):
    if request.method == 'POST':
        form=ResetPasswordForm(request.POST)
        if form.is_valid():
            otp=form.cleaned_data['otp']
            email=form.cleaned_data['email']
            user = Register.objects.get(email=email)
            user_otp=Reset.objects.filter(user=user).first()
            if user_otp.otp == otp:
                newpassword=form.cleaned_data['new_password']
                data=Register.objects.get(id=user.id)
                data.password=make_password(newpassword)
                data.save()

                user_otp.delete()

                messages.success(request,"Password changed", extra_tags="success")
                return redirect('user_login')
            else:
                messages.error(request,"Inavalid otp", extra_tags="error")
        else:
            messages.error(request,"Inavalid form data", extra_tags="error")
    else:
        form=ResetPasswordForm()
    return render(request,'reset_password.html',{'form':form})














# def calculate_cover_amount(age): #Example logic
#     if age < 30:
#         return 100000
#     elif age < 40:
#         return 200000
#     elif age < 50:
#         return 300000
#     else:
#         return 400000


def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES) # Add request.FILES
        if form.is_valid():
            try:
                policy = form.save(commit=False)
                # policy.price = calculate_policy_price(policy.age)
                # policy.cover_amount = calculate_cover_amount(policy.age)
                # policy.no_months = calculate_no_months(policy.age)
                # policy.total_amnt = calculate_total_amnt(policy.age)
                policy.created_by = request.user
                policy.save()
                messages.success(request, "Policy added successfully!")
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)}, status=400)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            return JsonResponse({'success': False, 'message': errors}, status=400)
    else:
        form = PolicyForm()
    return render(request, 'add_policy.html', {'form': form})
#Update your edit_policy view

def view_policy(request):
    # policy=Policy.objects.filter(usertype="policy")
    return render(request,'view_policy.html',{'policy':Policy})


def approve_policy(request,id):
    policy=Policy.objects.get(id=id)
    policy.is_approved=True
    policy.save()
    messages.success(request,'policy approved successfully',extra_tags="success")
    return redirect('view_policy')


def reject_policy(request,id):
    policy=Policy.objects.get(id=id)
    subject="Account Rejection Notification"
    message=f"Dear {policy.name} Your registration is being Rejected. Please register again with valid details for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[policy.email]
    send_mail(subject, message, email_from, email_to)

    policy.delete()
    messages.success(request,'policy rejected successfully',extra_tags='success')
    return redirect('view_policy')










def edit_policy(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)

    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES, instance=policy)  # CRUCIAL CHANGE: ADD request.FILES
        if form.is_valid():
            policy = form.save(commit=False)
            policy.save()
            messages.success(request, "Policy updated successfully!")
            return redirect('policy_detail', policy_id=policy.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'edit_policy.html', {'form': form, 'policy': policy})

    else:
        form = PolicyForm(instance=policy)

    return render(request, 'edit_policy.html', {'form': form, 'policy': policy})

def policy_list(request):
    policies = Policy.objects.all()  # Retrieve all policies
    return render(request, 'policy_list.html', {'policies': policies})



def policy_detail(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)  # Get policy or 404
    return render(request, 'policy_detail.html', {'policy': policy})



def user_policies(request):
    policies = Policy.objects.filter(created_by=request.user)
    return render(request, 'user_policies.html', {'policies': policies})

# def policy_view(request):
#     policies = Policy.objects.all() # Retrieve all policies from the database
#     context = {'policies': policies} # Create a context dictionary
#     return render(request, 'index.html', context) # Render the template with the context
def policy_overview(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)  # Get policy or 404
    return render(request, 'policy_overview.html', {'policy': policy})




def add_medical_info(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id) # Get the policy
    if request.method == 'POST':
        form = UserMedicalInfoForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            medical_info = form.save(commit=False)
            medical_info.policy = policy # Assign policy to the medical info
            medical_info.save()
            return redirect('policy_detail', policy_id=policy_id)  # Redirect to policy detail or wherever you want
    else:
        form = UserMedicalInfoForm()
    return render(request, 'add_medical_info.html', {'form': form, 'policy': policy}) # Pass policy context to the form.
