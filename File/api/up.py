from django.conf import settings

from File_up.models import File


def upload_check(data):
    format_file = str(data.get('file')).split('.')[-1]
    if format_file in settings.CORRECT_FORMATS:
        file = File.objects.filter(
            file=data.get('file')
        )
        file.processed = True
    return 0
