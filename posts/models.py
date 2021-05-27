from django.db import models



class Post(models.Model):
    name = models.CharField(max_length=14)
    body = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

