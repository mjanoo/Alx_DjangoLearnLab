from django.db import models

class Author(models.Model):
    """
    Author model:
    - Stores the author's name.
    - One Author can have many Book instances (one-to-many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: ForeignKey linking this book to an Author.
      An Author can have many Books (one-to-many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

