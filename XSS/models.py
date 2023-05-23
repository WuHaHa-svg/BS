import json

import requests
from django.db import models
import time


# Create your models here.


class XssResult(models.Model):
    url = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    grade = models.CharField(max_length=8, null=True)
    injection = models.CharField(max_length=255)
    task_created_time = models.DateTimeField(null=True, blank=True)
    task_begin_time = models.DateTimeField(null=True, blank=True)
    task_end_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(int(time.time() * 1000))
        super(XssResult, self).save(*args, **kwargs)
