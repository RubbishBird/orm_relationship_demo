from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse

def index(request):
    category = Category(category='小说')
    category.save()
    article = Article(name='红楼梦',author='曹雪芹')
    article.category = category
    article.save()
    return HttpResponse('success')
