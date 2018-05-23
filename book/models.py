import datetime

from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_info = models.TextField()
    isbn = ISBNField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    publish_date = models.DateTimeField(default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

