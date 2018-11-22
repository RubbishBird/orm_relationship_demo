from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

class Article(models.Model):
    #定义数据库字段
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    #设置表的外键
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    username = models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE,null=True)

