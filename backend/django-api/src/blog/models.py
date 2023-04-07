from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    avatar = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Category(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='categories')
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()
    published = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    post_fk = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

