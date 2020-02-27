from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import BookSerializer, BookUserSerializer
from .models import Book, BookUser           


class BookView(viewsets.ModelViewSet):
  serializer_class = BookSerializer 
  queryset = Book.objects.all()


class BookUserView(viewsets.ModelViewSet):
  serializer_class = BookUserSerializer 
  queryset = BookUser.objects.all()