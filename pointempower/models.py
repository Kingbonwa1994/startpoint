import datetime
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("")

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Client(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    expected_date = models.DateTimeField("start date")

    def __str__(self):
        return self.name