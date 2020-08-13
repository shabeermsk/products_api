from django.shortcuts import render
from .serializers import ProductSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductDetailUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.user.email)
        print(request.user.first_name)
        return super().get(request, *args, **kwargs)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class ProductUpdate(generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
