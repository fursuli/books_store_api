# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from bs_api.serializers import (AuthorSerializer,
                                BookSeralizer,
                                OrderSerializer
                                )

from bs_api.models import Author, Book, Order


class AuthorCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AllAuthorsView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSeralizer


class AllBooksView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSeralizer


class OrderCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AllOrdersView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
