from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import book_data
from django.shortcuts import render


def detail_book(request, book_id):
    context = {'book': book_data[book_id - 1]}
    return render(request, 'books/detail.html', context)


def list_books(request):
    context = {"book_list": book_data}
    return render(request, 'books/index.html', context)


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
        book_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'capa_url': request.POST['capa_url']
        })
        return HttpResponseRedirect(
            reverse('books:detail', args=(len(book_data), )))
    else:
        return render(request, 'books/create.html', {})
