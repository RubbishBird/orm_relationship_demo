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

    # 更改表名
    # class Meta:
    #     db_table='article'


class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self',on_delete=models.CASCADE)
