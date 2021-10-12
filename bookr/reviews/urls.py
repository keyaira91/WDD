from django.contrib import admin
from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # Homepage
    # path('', views.index, name='index'),

    # Search Page
    # path('book-search', views.search, name='book-search')

    path('', views.welcome_view, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:details_id>', views.book_details, name='book_details')
]