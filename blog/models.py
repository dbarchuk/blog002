from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_cteation = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
