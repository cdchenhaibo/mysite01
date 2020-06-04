from django.db import models
from django.utils import timezone


# Create your models here.


class FileInfo(models.Model):
    file_name = models.CharField(max_length=500)
    file_title = models.CharField(max_length=500, blank=True, null=True)
    file_size = models.DecimalField(max_digits=10, decimal_places=0)
    file_path = models.CharField(max_length=500)
    upload_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.file_name
