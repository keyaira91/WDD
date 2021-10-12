from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from .utils import average_rating


def welcome_view(request):
    # message = f"<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
    return render(request, 'base.html')

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,\
                    'book_rating': book_rating,\
                    'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'book_list.html', context)

def book_details(request, details_id):
    # details = Book.objects.get(id=details_id)
    details = get_object_or_404(Book, id=details_id)
    comments = details.review_set.order_by('date_created')
    context = {'details': details, 'comments': comments}
    return render(request, 'book_details.html', context)