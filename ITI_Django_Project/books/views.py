from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views import View
from books.forms import booksModelForm
from books.models import books
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from students.models import BorrowedBook

# Create your views here.
class CreateAllbooksView(View):

    def get(self, request):
        form = booksModelForm()
        return render(request, 'books/create.html', {'form': form})

    def post(self, request):
        form =booksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("object added")

        return render(request, 'books/create.html', {'form': form})


class CreatebooksGenericView(CreateView):
    form_class = booksModelForm
    template_name = 'books/create.html'
    success_url = '/book/home/'


class booksListGenericView(ListView):
    model = books
    template_name = 'books/index.html'
    context_object_name = 'books'

    #  to display some

    # def queryset(self):
    #     return Categories.objects.filter(id__gt=7)


class booksDetailGenericView(DetailView):
    model = books
    template_name = 'books/show.html'


class UpdatebooksGenericView(UpdateView):
    model = books
    form_class = booksModelForm
    template_name = 'books/edit.html'
    success_url = '../home'


class DeletebooksGenericView(DeleteView):
    model = books
    template_name = 'books/delete.html'
    success_url = '../home'



def view(request):
    all_borrowed_books = BorrowedBook.objects.all()
    return render(request, 'booksborrowed.html', {'all_borrowed_books': all_borrowed_books})
