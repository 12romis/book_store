import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response

from book.models import Book


def index(request):
    try:
        ord = int(request.GET.get('order', 0))
    except ValueError:
        ord = 1
    if ord:
        order = 'publish_date'
    else:
        order = '-publish_date'
    page = request.GET.get('p', 1)

    books = Book.objects.order_by(order)

    paginator = Paginator(books, 10)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    data = {'books': items,
            'year': datetime.datetime.now().year,
            'order': ord
            }
    return render_to_response('index.html', data)


def book(request, *args, **kwargs):
    return render_to_response('book.html')
