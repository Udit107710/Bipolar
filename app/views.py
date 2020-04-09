from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions  import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from app.models import Book, Reader
from app.serializers import BookSerializer, ReaderSerializer

class BookView(ModelViewSet):
    """
    ViewSet to map CRUD operations to Book model.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderView(ModelViewSet):
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