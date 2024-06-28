from django.urls import path
from .views import BookDetailAPIView,BookDetailListAPIView

urlpatterns = [
    path('book-details/', BookDetailAPIView.as_view(), name='book-detail-create'),  # For POST method
    path('book-details/<uuid:book_id>/', BookDetailAPIView.as_view(), name='book-detail-retrieve-update-delete'),  # For GET, PUT, DELETE methods
     path('book-details/all/', BookDetailListAPIView.as_view(), name='book-detail-list'),
]