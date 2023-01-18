from django.urls import path
from .views import books

app_name = "book"

urlpatterns = [
    path("books/", books, name="book-list"),
]
