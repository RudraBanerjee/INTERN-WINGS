from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=400,blank=True, null=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    DOB=models.DateField()
    # USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['password']

    def __str__(self):
        return self.username
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    Catagories = models.CharField(max_length=255, default = "Others")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment_content = models.TextField(null = False)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'