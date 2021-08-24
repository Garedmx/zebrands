from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product
from .forms import UserModelForm, ProductModelForm


class HomeView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()


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

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, id=id_)


class ProductEdit(generic.UpdateView):
    template_name = 'edit_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('home')
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['something'] = Product.objects.get(pk=self.kwargs.get('pk')).pk
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, id=id_)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductEdit, self).dispatch(*args, **kwargs)


class UserEdit(generic.UpdateView):
    template_name = 'edit_user.html'
    form_class = UserModelForm
    success_url = reverse_lazy('users')
    queryset = User.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(User, id=id_)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserEdit, self).dispatch(*args, **kwargs)


class UserDelete(generic.DeleteView):
    template_name = 'delete_user.html'
    success_url = reverse_lazy('users')
    queryset = User.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(User, id=id_)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDelete, self).dispatch(*args, **kwargs)


class ProductDelete(generic.DeleteView):
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, id=id_)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductDelete, self).dispatch(*args, **kwargs)