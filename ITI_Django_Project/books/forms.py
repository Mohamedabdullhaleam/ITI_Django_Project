from django import forms
from books.models import books


class booksModelForm(forms.ModelForm):
    class Meta:
        model = books
        fields = '__all__'


    def clean_name(self):
        name = self.cleaned_data['name']
        if books.objects.filter(name=name).exists():
            raise forms.ValidationError("This name already exists")
        return name
