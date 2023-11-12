from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import book_data
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import BookForm
from .models import Book, Review
from .forms import BookForm, ReviewForm
from django.urls import reverse, reverse_lazy
from .models import Book, Review, List
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

def list_books(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    last_book_id = request.session.get('last_viewed', None)
    if last_book_id:
        context["last_book"] = Book.objects.get(pk=last_book_id)
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

def create_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            book.review_set.create(author=review_author, text=review_text)
            return HttpResponseRedirect(
                reverse('books:detail', args=(pk, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'book': book}
    return render(request, 'books/review.html', context)


@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = request.user 


def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    request.session['last_viewed'] = book_id
    context = {'book': book}
    return render(request, 'books/detail.html', context)



class ListListView(generic.ListView):
    model = List
    template_name = 'books/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'books/create_list.html'
    fields = ['name', 'author', 'books']
    success_url = reverse_lazy('books:lists')
