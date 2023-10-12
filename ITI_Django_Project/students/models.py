from django.db import models

# Create your models here.
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.db import models
from books.models import books

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    auther = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)



    # def __str__(self):
    #     return f'{self.name}'
