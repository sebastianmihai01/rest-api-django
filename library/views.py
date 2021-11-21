from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# Custom Code -> ViewSets (Like YouTube IMDb API I made)
# Generic CRUD -> Generics (below)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #auth
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
