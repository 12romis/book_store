from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from book.models import Book


class BookForm(forms.ModelForm):
    publish_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Book
        fields = '__all__'

