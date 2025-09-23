from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListCreateView, BookDetailView, BookViewSet

# Router for ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Generic views (current quiz step)
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # ViewSet routes
    path("", include(router.urls)),

    # Token authentication endpoint
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
