from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import reverse



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    @classmethod
    def get_all_RegistrationForm(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_RegistrationForm(cls, id):
        return cls.objects.get(id=id)

    def get_edit_url(user):
        return reverse('users.edit', args=[user.id])
