from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from books.models import Books
from .serializers import BookSerializer
from api import serializers

@api_view()
def api_view(request):  # request of rest_framework
    return Response('OK')  # response of rest_framework


class BooksList(APIView):
    def get(self,request):
        queryset = Books.objects.all()
        serializer = BookSerializer(
            queryset, many=True, context={'request':request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetail(APIView):
    def get(self, request, id):
        book = get_object_or_404(Books, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, id):
        book = get_object_or_404(Books, pk=id)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        book = get_object_or_404(Books, pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


