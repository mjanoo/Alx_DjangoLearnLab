from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-Based View: list all books
    path("books/", list_books, name="list_books"),

    # Class-Based View: show library details
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
