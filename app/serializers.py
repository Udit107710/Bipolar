from rest_framework import serializers
from app.models import Book, Reader

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Book model.
    Attributes:
        title: str
        amazon_url: url
        author: str
        genre: str
    """

    class Meta:
        model = Book
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    """
    Serializer class for Reader model.
    Attributes:
        user: User
        books: list[Book]
    """

    class Meta:
        model = Reader
        fields = ('books',)
        read_only_field = ('user',)
