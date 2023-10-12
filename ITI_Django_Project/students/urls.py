# source_app/urls.py
from django.urls import path
from . import views
from .views import show , UserListGenericView ,view ,UpdateUserGenericView

urlpatterns = [

    path('allbooks/', view, name='all_books'),
    path('<int:book_id>', show, name='show'),
    path('index/', UserListGenericView.as_view(), name='uesr.info'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrowed/', views.borrowed_books, name='borrowed_books'),
    path('<int:pk>/edit', UpdateUserGenericView.as_view(), name='update.user'),


]
