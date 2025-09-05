from django.urls import path
from . import views  # import views from this app

urlpatterns = [
    # Function-Based View: list all books
    path("books/", views.list_books, name="list_books"),

    # Class-Based View: show library details
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
