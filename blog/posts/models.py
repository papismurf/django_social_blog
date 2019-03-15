from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    creator = models.ForeignKey(User, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
