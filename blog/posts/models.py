from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    creator = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.SET_NULL,
        null=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    upvotes = models.ManyToManyField(User, through='Upvote')


class Upvote(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)
