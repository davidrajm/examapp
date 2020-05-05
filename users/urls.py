from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='user-logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='user-password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'), #Dont change the name as django needs the exact name
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'), #Dont change the name as django needs the exact name
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),#Dont change the name as django needs the exact name
    path('profile/', views.profile, name='user-profile'),
]
