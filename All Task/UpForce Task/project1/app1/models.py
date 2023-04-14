from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.post}---{self.user}'
