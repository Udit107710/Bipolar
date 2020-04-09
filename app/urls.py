from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.routers import CustomRouter
from app.views import ReaderView, BookView

reader_router = CustomRouter()
reader_router.register('reader', ReaderView)

book_router = DefaultRouter()
book_router.register('book', BookView)

urlpatterns = [
]

urlpatterns += book_router.urls
urlpatterns += reader_router.urls
