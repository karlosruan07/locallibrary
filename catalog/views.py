
from django.shortcuts import render
from django.http import Http404

from .models import Book, BookInstance, BookIdioma, Author, Genre

from django.views import generic

from catalog import models

def index(request):

    num_book = Book.objects.all().count()
    num_instance = Book.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='m').count()
    num_author = Author.objects.all().count()
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1

    contexto = {

        "num_book" : num_book,
        "num_instance" : num_instance,
        "num_instance_available" : num_instance_available,
        "num_author" : num_author,
        "num_visitas" : num_visitas,
        
    }
    return render(request, 'catalog/index.html', context=contexto)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)#obtem o contexto existente da superclasse.
        context['info'] = 'info'#adicionando mais informações no contexto
        return context #retornando o contexto atualizado, isso é obrigatório


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['info'] = 'info'
        return context

