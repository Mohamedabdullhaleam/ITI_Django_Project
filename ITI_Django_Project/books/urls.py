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
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from books.views import ( CreatebooksGenericView
                         , booksListGenericView, booksDetailGenericView
                         ,UpdatebooksGenericView, DeletebooksGenericView)


urlpatterns = [
    path('create/generic', CreatebooksGenericView.as_view(), name='books.create'),
    path('home/', booksListGenericView.as_view(), name='books.index'),
    path('<int:pk>', booksDetailGenericView.as_view(), name='books.show'),
    path('<int:pk>/edit',UpdatebooksGenericView.as_view(), name='books.edit'),
    path('<int:pk>/delete', DeletebooksGenericView.as_view(), name='books.delete'),
    path('borrowedbooks/', views.view, name='borrowed_books'),
]
