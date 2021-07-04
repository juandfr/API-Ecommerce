from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ApiApp import serializers
from ApiApp import models


class BookViewSet(viewsets.ModelViewSet):

    #permission_classes = (IsAuthenticated, )

    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):

    #permission_classes = (IsAuthenticated, )

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):

    #permission_classes = (IsAuthenticated, )

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()