from __future__ import unicode_literals
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
