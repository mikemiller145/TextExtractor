from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

class Upload(models.Model):
    title = models.CharField(max_length=100, default='title')
    file = models.FileField(upload_to='uploads/%Y/%m/%d')
    user = models.ForeignKey(User, default="1", on_delete=models.CASCADE)


class Data(models.Model):
    word = models.CharField(max_length=100)
    count = models.IntegerField()
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)