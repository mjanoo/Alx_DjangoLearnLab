from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
from relationship_app.models import Author, Book

def get_books_by_author(author_name):
    # Step 1: Get the Author object
    author = Author.objects.get(name=author_name)

    # Step 2: Get all Books by that Author
    return Book.objects.filter(author=author)


# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
