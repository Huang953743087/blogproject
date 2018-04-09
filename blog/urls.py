#!usr/bin/python3
#-*- coding:utf-8 -*-

from django.conf.urls import url
from django.urls import re_path, path

from blog.views import CategoryView, ArchiveView, DetailView, TagView, AboutView, ConnectView

app_name='blog'
urlpatterns = [

    # 文章详情页
    re_path('post/(?P<pk>[0-9]+)/', DetailView.as_view(),name='detail'),
    # 按年月查找
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', ArchiveView.as_view(), name='archives'),
    # 按分类查找
    re_path('category/(?P<pk>[0-9]+)/', CategoryView.as_view(), name='category'),
    # 按分类查找
    re_path('tag/(?P<pk>[0-9]+)/', TagView.as_view(), name='tag'),
    path('about/', AboutView.as_view(), name='about'),
    path('connect/', ConnectView.as_view(), name='connect')
]
