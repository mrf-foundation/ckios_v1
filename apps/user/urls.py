# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.user import views as user_views
from.views import EditProfilePage


urlpatterns = [
    #User
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path("myprofile/", user_views.myprofile, name="Myprofile"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('tinymce/', include('tinymce.urls')),
    path('edit_profile_page/', user_views.EditProfilePage.as_view(template_name='registration/edit_profile_page.html'), name='edit_profile_page'),
    # For PasswordPresset

    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset',),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
]