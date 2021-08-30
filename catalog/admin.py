from django.contrib import admin
from django.db import models
from catalog.models import Genre, Book, BookInstance, Author, BookIdioma


admin.site.register(Genre)
admin.site.register(BookIdioma)

@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]#define quais campos serão exibidos  



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


