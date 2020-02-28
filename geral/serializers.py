from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "author", "title", "description", "created_date"]


class BookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUser
        fields = ["id"]