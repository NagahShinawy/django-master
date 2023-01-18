from django.urls import path
from .views import (
    cfh,
    products_list,
    create_product,
    ProductDetailAPIView,
    ProductListAPIView,
    ProductCreateAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductMixinView,
    ColorListCreateAPIView,
    BikeListAPIView,
)


app_name = "product"


urlpatterns = [
    path("api/v1/cfe/", cfh, name="cfe"),
    path("api/v1/bikes/", BikeListAPIView.as_view(), name="bikes"),
    path("api/v1/colors/", ColorListCreateAPIView.as_view(), name="colors"),
    path("api/v1/products_list/", products_list, name="products_list"),
    path("api/v1/products/create/", create_product, name="create"),
    path("api/v1/products/<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
    path(
        "api/v1/products/update/<int:pk>/",
        ProductUpdateAPIView.as_view(),
        name="update",
    ),
    path(
        "api/v1/products/delete/<int:pk>/",
        ProductDeleteAPIView.as_view(),
        name="delete",
    ),
    path("api/v1/products/", ProductListAPIView.as_view(), name="products-list"),
    path("api/v1/products/add/", ProductCreateAPIView.as_view(), name="add"),
    path(
        "api/v1/products/list-create/<int:pk>/",
        ProductMixinView.as_view(),
        name="list-create",
    ),
    path(
        "api/v1/products/add-list/", ProductListCreateAPIView.as_view(), name="add-list"
    ),
    path("api/v1/products/list/", ProductListAPIView.as_view(), name="list"),
]
