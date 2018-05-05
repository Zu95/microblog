from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    brief = models.TextField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='category_images')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name