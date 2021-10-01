from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Search Page
    path('book-search', views.search, name='book-search')
]