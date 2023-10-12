from django.shortcuts import render,redirect
from adminss.forms import RegistrationForm
from django.views.generic import ListView
from adminss.forms import User
from django.contrib.auth.models import User
# Create your views here.
from students.models import BorrowedBook

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
class UserListGenericView(ListView):
    model = User
    template_name = 'adminss/index.html'
    context_object_name = 'users'
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def borrowed_books(request):

    user_borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'all_borrowed_books.html', {'borrowed_books': user_borrowed_books})