from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import BookDetailSerializer



# |================================= Tag APIs =============================| #

class BookDetailListAPIView(GenericAPIView):
    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()

    def get(self, request, *args, **kwargs):
        book_details = self.get_queryset()
        serializer = self.serializer_class(book_details, many=True)
        return Response({
            "message": "Book details retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    

# |================================= Tag APIs =============================| #


class BookDetailAPIView(GenericAPIView):
    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()

    def get_object(self, book_id):
        try:
            return BookDetail.objects.get(uid=book_id)
        except BookDetail.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            book_detail = serializer.save()
            return Response({
                "message": "Book details saved successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, book_id, *args, **kwargs):
        book_detail = self.get_object(book_id)
        if not book_detail:
            return Response({"message": "BookDetail not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(book_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Book details updated successfully",
                "data": serializer.data
            })
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, book_id, *args, **kwargs):
        book_detail = self.get_object(book_id)
        if not book_detail:
            return Response({"message": "BookDetail not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(book_detail)
        return Response({
            "message": "Book details retrieved successfully",
            "data": serializer.data
        })

    def delete(self, request, book_id, *args, **kwargs):
        book_detail = self.get_object(book_id)
        if not book_detail:
            return Response({"message": "BookDetail not found"}, status=status.HTTP_404_NOT_FOUND)

        book_detail.delete()
        return Response({
            "message": "Book details deleted successfully",
        }, status=status.HTTP_204_NO_CONTENT)
