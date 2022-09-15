from tkinter import CASCADE
from django.db import models
from authentication.models import User

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    video_id = models.CharField(max_length=250, null=True)
    text = models.CharField(max_length=250, null=True)
    likes = models.IntegerField(default=0)
    dislikes =models.IntegerField(default=0)

