from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class books(models.Model):
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_books(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_books(cls, id):
        return cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('books.show', args=[self.id])

    def get_delete_url(self):
        return reverse('books.delete', args=[self.id])

    def get_edit_url(self):
        return reverse('books.edit', args=[self.id])
