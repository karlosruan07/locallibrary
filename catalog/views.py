
from django.shortcuts import render

from .models import Book, BookInstance, BookIdioma, Author, Genre

def index(request):

    num_book = Book.objects.all().count()
    num_instance = Book.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='m').count()
    num_author = Author.objects.all().count()

    contexto = {

        "num_book" : num_book,
        "num_instance" : num_instance,
        "num_instance_available" : num_instance_available,
        "num_author" : num_author
    }
    return render(request, 'base.html')


def all_books(request):
    num_book = Book.objects.all().count()
    contexto = {"num_book":num_book}
    return render(request, 'catalog/books.html',context=contexto)
