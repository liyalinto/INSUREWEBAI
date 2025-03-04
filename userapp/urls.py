from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('login',views.user_login,name="user_login"),
    path('register',views.register),
    path('about',views.about),
    path('insurance',views.insurance),
    path('services',views.services),
    path('contact',views.contact),
    path('view_user',views.view_user,name="view_user"),
    path('view_staff',views.view_staff,name="view_staff"),
    path('view_hospital',views.view_hospital,name="view_hospital"),
    path('profile',views.profile,name="profile"),
    path('staff_profile',views.staff_profile,name="profile"),
    path('hospital_profile',views.hospital_profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('delete_user/<int:id>/',views.delete_user,name="delete_user"),
    path('delete_staff/<int:id>/',views.delete_staff,name="delete_staff"),
    path('delete_hospital/<int:id>/',views.delete_hospital,name="delete_hospital"),
    path('approve_staff/<int:id>/',views.approve_staff,name="approve_staff"),
    path('reject_staff/<int:id>/',views.reject_staff,name="reject_staff"),
    path('approve_user/<int:id>/',views.approve_user,name="approve_user"),
    path('reject_user/<int:id>/',views.reject_user,name="reject_user"),
    path('approve_hospital/<int:id>/',views.approve_hospital,name="approve_hospital"),
    path('reject_hospital/<int:id>/',views.reject_hospital,name="reject_hospital"),
    path('staff_register',views.staffregister),
    path('hospital_register',views.hospital_register),
    path('registerationtype',views.registerationtype),
    path('staff_edit_profile',views.staff_edit_profile,name='staff_edit_profile'),
    path('hospital_edit_profile',views.hospital_edit_profile,name='hospital_edit_profile'),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('reset_password',views.reset_password,name="reset_password"),
    path('add_policy', views.add_policy, name='add_policy'),
    path('view_policy',views.view_policy,name="view_policy"),
    path('policy_list', views.policy_list, name='policy_list'),
    path('policy_detail/<int:policy_id>/', views.policy_detail, name='policy_detail'), #<int:policy_id> for the detail view
    path('edit_policy/<int:policy_id>/', views.edit_policy, name='edit_policy'),
    path('policy_overview/<int:policy_id>/', views.policy_overview, name='policy_overview'), #<int:policy_id> for the detail view
    path('policy/<int:policy_id>/add_medical_info/', views.add_medical_info, name='add_medical_info'),
    

]