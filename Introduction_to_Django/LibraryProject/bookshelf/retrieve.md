# Retrieve Book(s)

```python
# Retrieve all books
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve a single book by title
book = Book.objects.get(title="1984")
book
# <Book: 1984 by George Orwell (1949)>
```
# Retrieve Book(s)

```python
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
```
