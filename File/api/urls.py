from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    FileViewSet,
    ProcessedViewSet
)

router = DefaultRouter()

router.register('upload', FileViewSet, basename='upload')
router.register('files', ProcessedViewSet, basename='files')


urlpatterns = [
    path('', include(router.urls)),
]