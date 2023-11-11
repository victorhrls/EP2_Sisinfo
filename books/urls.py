from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.list_books, name='index'),
    path('search/', views.search_books, name='search'),
    path('create/', views.create_book, name='create'),
    path('<int:book_id>/', views.detail_book, name='detail'),
]
