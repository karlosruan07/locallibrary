
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-books/', views.all_books, name='all-books')
]


