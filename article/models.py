from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

