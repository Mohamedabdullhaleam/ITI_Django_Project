"""
URL configuration for djangoProjectt project.

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
from django.urls import path,include
from adminss.views import profile,register,UserListGenericView,user_list,borrowed_books
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('/profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('index/', UserListGenericView.as_view(), name='uesrs.html'),
    path('adminstration/logout/',profile,name='log'),
    path('users/', user_list, name='user_list'),
    path('borrowed-books/', borrowed_books, name='all_borrowed_books'),
]
