from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    # Function-Based View: list all books
    path("books/", list_books, name="list_books"),

    # Class-Based View: show library details
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication Views
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
