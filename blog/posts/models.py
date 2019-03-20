from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import pluralize


class Posts(models.Model):
    """
    Model for User Posts
    """
    creator = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.SET_NULL,
        null=True
    )
    publication_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    title = models.CharField(max_length=256)
    upvotes = models.ManyToManyField(User, through='PostUpvote', related_name='posts_upvotes')

    # Method to show time since post was published
    def how_long_ago(self):
        how_long = datetime.now() - self.publication_date
        if how_long < timedelta(minutes=1):
            return f'{how_long.seconds} second{pluralize(how_long.seconds)} ago'
        elif how_long < timedelta(hours=1):
            minutes = int(how_long.total_seconds()) // 60
            return f'{minutes} minute{pluralize(minutes)} ago'
        elif how_long < timedelta(days=1):
            hours = int(how_long.total_seconds()) // 3600
            return f'{hours} hour{pluralize(hours)} ago'
        else:
            return f'{how_long.days} day{pluralize(how_long.days)} ago'


class PostUpvote(models.Model):
    """Model for Upvotes on a Post"""
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Model for Individual comments on Posts
    """
    publication_date = models.DateTimeField(auto_now_add=True)
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
    """
    Model for Upvotes on individual comments
    """
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_upvotes', on_delete=models.CASCADE)
