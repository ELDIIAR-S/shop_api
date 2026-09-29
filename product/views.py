from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


# --- Categories ---
@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_api_view(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# --- Products ---
@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# --- Reviews ---
@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data, status=status.HTTP_200_OK)



# from rest_framework import generics
#
# from .models import Category, Product, Review
# from .serializers import (
#     CategorySerializer,
#     ProductSerializer,
#     ReviewSerializer
# )
#
#
# # Categories
#
# class CategoryListAPIView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDetailAPIView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# # Products
#
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# # Reviews
#
# class ReviewListAPIView(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class ReviewDetailAPIView(generics.RetrieveAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer