from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.category_list_api_view),
    path('categories/<int:id>/', views.category_detail_api_view),

    # Products
    path('products/', views.product_list_api_view),
    path('products/<int:id>/', views.product_detail_api_view),

    # Reviews
    path('reviews/', views.review_list_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
]


# from django.urls import path
#
# from .views import *
#
#
# urlpatterns = [
#
#     path(
#         "categories/",
#         CategoryListAPIView.as_view()
#     ),
#
#     path(
#         "categories/<int:id>/",
#         CategoryDetailAPIView.as_view()
#     ),
#
#
#     path(
#         "products/",
#         ProductListAPIView.as_view()
#     ),
#
#     path(
#         "products/<int:pk>/",
#         ProductDetailAPIView.as_view()
#     ),
#
#
#     path(
#         "reviews/",
#         ReviewListAPIView.as_view()
#     ),
#
#     path(
#         "reviews/<int:pk>/",
#         ReviewDetailAPIView.as_view()
#     ),
# ]