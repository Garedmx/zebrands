from django.shortcuts import render
from django.views import generic
from .models import Product


class HomeView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()
