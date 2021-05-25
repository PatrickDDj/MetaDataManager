"""MetaDataManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_table', views.create_table, name='create_table'),
    path('to_create_table', views.to_create_table, name='to_create_table'),
    path('show_records/<str:table_name>', views.show_records, name='show_records'),
    path('add_record/<str:table_name>', views.add_record, name='add_record'),
    path('delete_table/<str:table_name>', views.delete_table, name='delete_table'),
    path('delete_record/<str:table_name>/<int:index>', views.delete_record, name='delete_record'),
    path('edit_record/<str:table_name>/<int:index>', views.edit_record, name='edit_record'),
]
