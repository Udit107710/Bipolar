from django.db import models
from django.contrib.auth.models import User

from multiselectfield import MultiSelectField


class Book(models.Model):
    """
    Model to represent a book.
    Attribute:
        title: str
        amazon_url: url
        author: str
        genre: crime
    """

    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('sci-fi', 'Sci-Fi'),
        ('thiller', 'Thriller'),
        ('adventure', 'Adventure'),
        ('crime', ('Crime'))
    )
    
    title = models.CharField(max_length=70)
    amazon_url = models.URLField(max_length=200)
    author = models.CharField(max_length=50)
    genre = MultiSelectField(choices=GENRE_CHOICES)


class Reader(models.Model):
    """
    Model to represent a reader.
    Attribute:
        user: User
        books: list[Book]
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    books = models.ManyToManyField(Book)
