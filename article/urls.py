from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('',views.index1,name='index1')
]