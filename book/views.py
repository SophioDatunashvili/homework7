from django.shortcuts import render
from .models import Book


# Create your views here.
def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html', {'book': book})
