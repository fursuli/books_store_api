from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path

from bs_api.views import AuthorRUDView, BookRUDView, OrderRUDView, AuthorCreateView, BookCreateView, OrderCreateView, \
    AllAuthorsView, AllBooksView, AllOrdersView

urlpatterns = [
    path('authors/<int:pk>/edit/', AuthorRUDView.as_view()),
    path('books/<int:pk>/edit/', BookRUDView.as_view()),
    path('orders/<int:pk>/edit/', OrderRUDView.as_view()),
    path('authors/create/', AuthorCreateView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('authors/', AllAuthorsView.as_view()),
    path('books/', AllBooksView.as_view()),
    path('orders/', AllOrdersView.as_view()),
]