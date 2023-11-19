"""
URL configuration for diucms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from main_app.views import edit_counselling_hour, register_user, welcome, profile, user_login, request_slot, update_approve, find_schedule, delete_slot

urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
    path('sign_up/', register_user),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('request_slot/', request_slot, name='request_slot'),
    path('update_approve/', update_approve, name='update_approve'),
    path('edit_counselling_hour/', edit_counselling_hour, name='edit_counselling_hour'),
    path('find_schedule/', find_schedule, name='find_schedule'),
    path('delete_slot/', delete_slot, name='delete_slot'),
]
