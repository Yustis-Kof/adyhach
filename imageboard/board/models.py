from django.db import models
from django.utils import timezone

class Board(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=50)
    last = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.code

class Thread(models.Model):
    title = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    last = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    local_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content

class Attachment(models.Model):
    file = models.FileField(upload_to="attachments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

