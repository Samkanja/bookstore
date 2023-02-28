from django.shortcuts import render

# Create your views here.

from .models import Book
from django.views.generic import ListView
from .utils import average_rating


class BookListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = context['object_list']
        book_list = []
        for book in books:
            reviews = book.review_set.all()
            if reviews:
                book_rating = average_rating([review.rating for review in reviews])
                number_of_reviews = len(reviews)
            else:
                book_rating = None
                number_of_reviews = 0
            book_list.append({'book':book,'book_rating':book_rating,'number_of_reviews':number_of_reviews})
        context['book_list'] = book_list
        return context


