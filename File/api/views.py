from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from File_up.models import File
from .serializers import FileSerializer
from .tasks import check_file

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            check_file(data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcessedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all().order_by('file')
    serializer_class = FileSerializer
    filter_backends = [DjangoFilterBackend, ]
    http_method_names = ['get',]
