from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# List all books / Create a new book
# -------------------------------
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# -------------------------------
# Retrieve / Update / Delete a book by ID
# -------------------------------
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can update or delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
