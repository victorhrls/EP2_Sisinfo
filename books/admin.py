
# Register your models here.

from django.contrib import admin

from .models import Book, Review, List

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(List)