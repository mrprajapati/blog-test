from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    publish_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
