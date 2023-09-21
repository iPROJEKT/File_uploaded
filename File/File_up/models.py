from django.db import models
from django.conf import settings
from django.utils import timezone


class File(models.Model):
    file = models.FileField(
        upload_to=settings.PATH_UPLOAD,
        blank=False,
        null=False,
        max_length=settings.MAX_NAME_LENGHT
    )
    uploaded_at = models.DateTimeField(
        blank=True,
        default=timezone.now
    )
    processed = models.BooleanField()

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
