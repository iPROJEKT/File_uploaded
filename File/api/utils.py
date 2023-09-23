from django.conf import settings

from File_up.models import File


def upload_check(data):
    file = File.objects.filter(
        file=data.get('file')
    )
    try:
        with open(file, "w") as f:
            f.read(0)
    except Exception:
        raise Exception
    file.processed = True
    return 0
