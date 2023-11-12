from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import book_data
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.views import generic



class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/index.html'


def search_books(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "book_list": [
                m for m in book_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'books/search.html', context)


def create_book(request):
    if request.method == 'POST':
        book_name = request.POST['name']
        book_release_year = request.POST['release_year']
        book_capa_url = request.POST['capa_url']
        book = Book(name=book_name,
                      release_year=book_release_year,
                      capa_url=book_capa_url)
        book.save()
        return HttpResponseRedirect(reverse('books:detail',
                                            args=(book.id, )))
    else:
        return render(request, 'books/create.html', {})

def list_books(request):
    book_list = Book.objects.all()
    context = {"book_list": book_list}
    return render(request, 'books/index.html', context)