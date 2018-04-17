#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'huang'
__time__ = '2018/4/17 17:02'

from django.contrib.syndication.views import Feed

from blog.models import Post


class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "黄泽昊的博客"

    # 通过聚合阅读器跳转到网站的地址
    link = "http://119.29.139.42/"

    # 显示在聚合阅读器上的描述信息
    description = "黄泽昊的博客站点"

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body
