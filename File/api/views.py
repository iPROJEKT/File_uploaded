from rest_framework import generics, status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Sum
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.permissions import(
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import APIView

from File_up.models import File
from .serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('file')
    serializer_class = FileSerializer
    filter_backends = [DjangoFilterBackend, ]
    http_method_names = ['post',]


class ProcessedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all().order_by('file')
    serializer_class = FileSerializer
    filter_backends = [DjangoFilterBackend, ]
    http_method_names = ['get',]
