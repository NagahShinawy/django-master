from apps.todoapi.api import urls as api_urls
from django.urls import path, include


urlpatterns = [
    path("api/v1", include(api_urls)),
]
