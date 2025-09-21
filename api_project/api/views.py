from rest_framework import viewsets, permissions, generics
from .models import Book
from .serializers import BookSerializer


# ✅ Add this back for the quiz check
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ✅ Keep your CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restricts access
