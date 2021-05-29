from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addBook',views.addBook),
    path('addAuthor',views.addAuthor),
    path('editBook/<int:book_id>',views.editBook),
    path('editBook/addAuthorToBook',views.addAuthorToBook),
    path('editBook/deleteAuthorFromBook',views.deleteAuthorFromBook),
    path('editAuthor/<int:author_id>',views.editAuthor),
    path('editAuthor/addBookToAuthor',views.addBookToAuthor),
    path('editAuthor/deleteBookFromAuthor',views.deleteBookFromAuthor),
]
