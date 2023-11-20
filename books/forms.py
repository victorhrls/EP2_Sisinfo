from django.forms import ModelForm
from .models import Book, Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'release_year',
            'capa_url',
            'categoria',
        ]
        labels = {
            "name": "Título",
            "categoria": "Ano de publicação",
            "capa_url": "URL da Imagem",
            "categoria": "Categoria de Livro"
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
        ]
        labels = {
            'text': 'Critica',
        }


