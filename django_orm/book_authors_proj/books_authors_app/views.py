from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context={
        'all_Books': Book.objects.all(),
        'all_Authors': Author.objects.all()
    }
    return render(request,"index.html",context)

def addBook(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def addAuthor(request):
    Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect('/')

def editBook(request,book_id):
    book=Book.objects.get(id=book_id)
    context={
        'book': book,
        'authors': book.authors.all(),
        'all_authors': Author.objects.all()
    }
    return render(request,"editBook.html",context)

def addAuthorToBook(request):
    book=Book.objects.get(id=request.POST['book_id'])
    author=Author.objects.get(id=request.POST['author_selected'])
    book.authors.add(author)
    return redirect(f'/editBook/{book.id}')

def deleteAuthorFromBook(request):
    book=Book.objects.get(id=request.POST['book_id'])
    author=Author.objects.get(id=request.POST['author_deleted'])
    book.authors.remove(author)
    return redirect(f'/editBook/{book.id}')

def editAuthor(request,author_id):
    author=Author.objects.get(id=author_id)
    context={
        'author': author,
        'books': author.books.all(),
        'all_books': Book.objects.all()
    }
    return render(request,"editAuthor.html",context)

def addBookToAuthor(request):
    author=Author.objects.get(id=request.POST['author_id'])
    book=Book.objects.get(id=request.POST['book_selected'])
    author.books.add(book)
    return redirect(f'/editAuthor/{author.id}')

def deleteBookFromAuthor(request):
    author=Author.objects.get(id=request.POST['author_id'])
    book=Book.objects.get(id=request.POST['book_deleted'])
    author.books.remove(book)
    return redirect(f'/editAuthor/{author.id}')