from django.contrib import admin
from biblioteca.models import Book, Author, Genre, Language


class Books(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', )
    link_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Book, Books)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
