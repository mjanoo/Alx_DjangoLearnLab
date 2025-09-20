from django.db import models

# Add bookshelf models here, e.g.:
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

