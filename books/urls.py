from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.list_books, name='index'), 
    path('search/', views.search_books, name='search'),
    path('create/', views.create_book, name='create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'), 
    path("update/<int:book_id>/", views.update_book, name="update"),
    path("delete/<int:book_id>/", views.delete_book, name="delete"),
    path('<int:pk>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
]
