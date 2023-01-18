from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.todoapi.api import urls as api_urls
from apps.bookapi import urls as book_api_urls
from django.urls import path, include


urlpatterns = [
    path("api/v1/", include(api_urls)),
    path("api/v1/", include(book_api_urls)),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name="refresh"),
]
