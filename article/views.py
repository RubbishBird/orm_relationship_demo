from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse

# def index(request):
#     category = Category(category='小说')
#     category.save()
#     article = Article(name='红楼梦',author='曹雪芹')
#     article.category = category
#     article.save()
#     return HttpResponse('success')

def index(requext):
    #在windows操作系统上，mysql的排序规则（collation）无论是什么，都是大小写不敏感的
    #在Linux操作系统上，Mysql的排序规则（collation）是utf8_bin，那么就是大小写敏感的
    #LiKE和=:大部分情况下是等价的，只有少数情况下是不等价的
    #exact和iexact：他们的区别其实就是Like和=的区别，因为exact会被翻译成=，而iexact会被翻译成Like
    article = Article.objects.filter(id__exact=1)
    print(type(article))
    return HttpResponse('success')

def index1(request):
    result = Article.objects.filter(name__contains='红楼梦')
    print(result.query)
    return HttpResponse('success')
