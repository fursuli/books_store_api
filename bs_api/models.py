# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=68)
    last_name = models.CharField(max_length=68)
    registration_date = models.DateField(default=timezone.now)
    birthday_date = models.DateField()
    key_words = models.CharField(max_length=68, blank=True, null=True)
    sales = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    languages = [
        ('ukr', 'Ukrainian'),
        ('eng', 'English'),
        ('grm', 'German'),
        ('frn', 'French')
    ]

    bindings = [
        ('Soft', 'Soft binding'),
        ('Hard', 'Hard binding')
    ]

    iSBNs = [
        ('9783161484100', '9783161484100'),
        ('2546854489720', '2546854489720'),
        ('7845124001454', '7845124001454'),
        ('6524408004012', '6524408004012')
    ]

    title = models.CharField(max_length=68, blank=True, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    reviews = models.TextField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=3, choices=languages, default='ukr', blank=True, null=True)
    publication_date = models.DateField(blank=False, null=False)
    binding = models.CharField(max_length=1, choices=bindings, blank=False, null=False)
    iSBN = models.CharField(max_length=13, choices=iSBNs, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.title}, {self.language}, {self.binding}'


class Order(models.Model):
    status_info = [
        ('inpr', 'in progress'),
        ('done', 'done'),
        ('canc', 'canceled')
    ]

    order_number = models.IntegerField(blank=False, null=True)
    purchased_books = models.ManyToManyField(to="Book", blank=False, related_name='purchased_books')
    order_date = models.DateField(blank=False, null=False)
    order_status = models.CharField(max_length=4, choices=status_info, blank=False, null=False)

    def __str__(self):
        return self.order_number

# class OrdersBooksRelation(models.Model):
#     queryset = Order.objects.prefetch_related('purchased_list')
