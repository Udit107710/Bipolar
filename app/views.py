from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions  import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from rest_framework import status

from app.models import Book, Reader
from app.serializers import BookSerializer, ReaderSerializer

class BookView(ModelViewSet):
    """
    ViewSet to map CRUD operations to Book model.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderView(ViewSet):
    """
    Viewset to map CRUD operations to Reader model.
    """

    authentication_class = (IsAuthenticated, )
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def perform_create(self, serializer: ReaderSerializer) -> None:
        serializer.save(user=self.request.user)

    def retrieve(self, request: Request) -> Response:
        """
        Get list of books of the current user.
        Args:
            request: Request
        
        Return:
            Response
        """
        data = get_object_or_404(self.queryset, user=self.request.user.id)
        serializer = ReaderSerializer(data)
        return Response(data=serializer.data)
    
    def delete(self, request: Request, pk: int) -> Response:
        """
        Delete a book entry from user's fav book list.
        Args:
            request: Request
            pk: PK of the book to be deleted

        Return:
            Response
        """
        print("helloo")
        book = get_object_or_404(Book, pk=pk)
        reader = get_object_or_404(Reader, user=request.user)
        reader.books.remove(book)
        print(reader.books, reader)
        serializer = ReaderSerializer(reader)
        return Response(data=serializer.data)

    def partial_update(self, request: Request, pk: int) -> Response:
        """
        Add a book to user's fav book list.
        Args:
            request: Request
            pk: PK of the book to be added
            
        Return:
            Response
        """
        book = get_object_or_404(Book, pk=pk)
        reader = get_object_or_404(Reader, user=request.user)
        reader.books.add(book)
        serializer = ReaderSerializer(reader)
        return Response(data=serializer.data)
    
    def update(self, request: Request) -> Response:
        """
        New list of user's fav books.
        Args:
            request: Request
        
        Return:
            Response
        """
        books = request.data["books"]
        reader = get_object_or_404(Reader, user=request.user)
        reader.books.clear()
        for book in books:
            b = get_object_or_404(Book, pk=str(book))
            reader.books.add(b)
        return Response(data=ReaderSerializer(reader).data)
