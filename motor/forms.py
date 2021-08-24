from django.forms import *
from django.contrib.auth.models import User
from .models import Product


class UserModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        )
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'email'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'placeholder': 'password'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return form


class ProductModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = (
            'name',
            'sku',
            'price',
            'brand',
            'description',
            'img',
            'quantity',
            'active'
        )
        widgets = {
            'id': HiddenInput,
            'name': TextInput(
                attrs={
                    'placeholder': 'Name Item'
                }
            ),
            'email': TextInput(
                attrs={
                    'sku': 'Unique SKU Item'
                }
            ),
            'brand': TextInput(
                attrs={
                    'placeholder': 'Brand Item'
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'active': CheckboxInput(
                attrs={
                    'placeholder': 'active'
                }
            ),
        }
