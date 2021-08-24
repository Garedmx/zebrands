from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import UserModelForm, ProductModelForm


class HomeView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()


class ProductEdit(generic.UpdateView):
    template_name = 'edit_product.html'
    model = Product

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductEdit, self).dispatch(*args, **kwargs)


class UserView(generic.ListView):
    template_name = 'list_user.html'
    queryset = User.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserView, self).dispatch(*args, **kwargs)


class UserAdd(generic.CreateView):
    template_name = 'add_user.html'
    form_class = UserModelForm
    success_url = reverse_lazy('users')
    model = User

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserAdd, self).dispatch(*args, **kwargs)


class ProductAdd(generic.CreateView):
    template_name = 'add_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('home')
    model = Product

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductAdd, self).dispatch(*args, **kwargs)


class ProductView(generic.DetailView):
    template_name = 'view_product.html'
    queryset = Product.objects.all()
