# Django CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # <Book: 1984 by George Orwell (1949)>
```

## Retrieve
```python
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
```

## Update
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  # <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## Delete
```python
book.delete()
Book.objects.all()
# <QuerySet []>
```
