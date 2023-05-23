from django.db import models
import time
from django.utils import timezone


# Create your models here.
class LogModel(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    message = models.TextField(max_length=2000)
    created_time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(int(time.time() * 1000))
        super(LogModel, self).save(*args, **kwargs)
