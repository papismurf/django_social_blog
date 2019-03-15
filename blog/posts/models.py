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
    title = models.CharField(max_length=256)
    upvotes = models.ManyToManyField(User, through='PostUpvote')


class PostUpvote(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)


class Comment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
    )
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE,
                               null=True, default=None)
    content = models.TextField(null=True)


class CommentUpvote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_upvotes', on_delete=models.CASCADE)
