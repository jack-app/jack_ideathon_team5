import datetime

from django.db import models
from django.utils import timezone

class Account(models.Model):
    username = models.CharField(max_length=200)
    password = models.DateTimeField('date published')
    def __str__(self):
        return self.username
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
