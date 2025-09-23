from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    BookListCreateView,
    BookDetailView,
    BookViewSet,
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

# Router for ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Combined List + Create
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    # Combined Detail (retrieve, update, delete)
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # ✅ Explicit generic class-based views
    path("books/list/", BookListView.as_view(), name="book-list-view"),
    path("books/create/", BookCreateView.as_view(), name="book-create-view"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update-view"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete-view"),

    # ViewSet routes
    path("", include(router.urls)),

    # Token authentication endpoint
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
