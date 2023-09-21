from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    upload_file,
    ProcessedViewSet
)

router = DefaultRouter()

router.register('files', ProcessedViewSet, basename='files')


urlpatterns = [
    path('', include(router.urls)),
    path('upload/', upload_file)
]