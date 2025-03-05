from django.db import models

class Demo(models.Model):
    ful_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)

    def __str__(self):
        return self.ful_name
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField()
    published_year=models.IntegerField()

    def __str__(self):
        return self.title
