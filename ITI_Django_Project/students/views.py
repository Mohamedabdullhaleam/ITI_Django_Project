from django.contrib.auth.models import User
from books.models import books
from django.shortcuts import render, redirect
from django.contrib import messages
from adminss.forms import RegistrationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from students.models import BorrowedBook
from .models import User
from django.contrib.auth.decorators import login_required



def view(request):
    all_books = books.objects.all()
    return render(request, 'home.html', {'all_books': all_books})


def show(request, book_id):
    book = books.objects.get(id=book_id)
    return render(request, 'show.html', context={'allbooks': book})


def iindex(request):
    allusers = RegistrationForm.objects.all()
    return render(request, 'student/allusers/iindex.html', {'RegistrationForm': allusers})



def borrow_book(request,book_id):
    if request.method == 'POST':
        book = books.objects.get(id=book_id)
        user = request.user

        if not BorrowedBook.objects.filter(user=user, book=book).exists():
            borrowed_book = BorrowedBook(user=user, book=book)
            borrowed_book.save()

        return redirect('all_books')

    return redirect('all_books')

def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

class UserListGenericView(ListView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'


class UpdateUserGenericView(UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = 'update.html'
    success_url = '../../adminstration/login/'






