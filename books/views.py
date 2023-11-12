from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import book_data
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import BookForm



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
        form =BookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['name']
            book_release_year = form.cleaned_data['release_year']
            book_capa_url = form.cleaned_data['capa_url']
            book = Book(name=book_name,
                          release_year=book_release_year,
                          capa_url=book_capa_url)
            book.save()
            return HttpResponseRedirect(
                reverse('books:detail', args=(book.id, )))
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'books/create.html', context)