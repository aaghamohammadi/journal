from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Item(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
