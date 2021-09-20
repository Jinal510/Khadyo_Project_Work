"""foodproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path('', views.home, name='home'),
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('reset-password/', views.reset_password, name='reset-password'),
   path('forgot-password/', views.forgot_password, name='forgot-password'),
   path('forgot-repassword/', views.forgot_repassword, name='forgot-repassword'),
   path('logout/', views.logout, name='logout'),
   path('food-supplier/', views.food_supplier, name='food-supplier'),
   path('profile-food-supplier/', views.profile_food_supplier, name='profile-food-supplier'),
   path('profile-ngo/', views.profile_ngo, name='profile-ngo'),
   path('update-profile/', views.update_profile, name='update-profile'),
   path('ngo-update-profile/', views.ngo_update_profile, name='ngo-update-profile'),
   path('add-food/', views.add_food, name='add-food'),
   path('view-food/', views.view_food, name='view-food'),
   path('view-food-details/<int:pk>', views.view_food_details, name='view-food-details'),
   path('ngo/', views.ngo, name='ngo'),
   path('feedback/',views.feedback, name='feedback'),
   path('view-feedback/', views.view_feedback, name='view-feedback'),
   path('contactus/',views.contactus, name='contactus'),
   path('paytmhome/',views.paytmhome, name="paytmhome"),
   path('initiate-payment/',views.initiate_payment, name="initiate-payment"),
   path('callback/',views.callback, name="callback"),
   #path('payment_view/',views.payment_view, name="payment_view"),
]
