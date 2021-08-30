from django.contrib import admin
from catalog.models import Genre, Book, BookInstance, Author, BookIdioma


admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(BookIdioma)
