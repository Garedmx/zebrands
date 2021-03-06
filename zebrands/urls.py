"""zebrands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from motor import views
from api import api

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_product/', views.ProductAdd.as_view(), name='add_product'),
    path('view_product/<int:pk>', views.ProductView.as_view(), name='view_product'),
    path('edit_product/<int:pk>', views.ProductEdit.as_view(), name='edit_product'),
    path('delete_product/<int:pk>', views.ProductDelete.as_view(), name='delete_product'),
    path('user/', views.UserView.as_view(), name='users'),
    path('add_user/', views.UserAdd.as_view(), name='add_user'),
    path('edit_user/<int:pk>', views.UserEdit.as_view(), name='edit_user'),
    path('delete_user/<int:pk>', views.UserDelete.as_view(), name='delete_user'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('api_info/', views.ApiInfo.as_view(), name='api_info'),
    path('api_products/', api.product_list, name='api_products'),
    path('api_detailes/<int:pk>', api.product_detail, name='api_detailes'),

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
