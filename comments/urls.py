#!/usr/bin/python3
#-*- coding: utf-8 -*-
from django.urls import re_path
from comments.views import CommentView

app_name = 'comments'
urlpatterns = [
       re_path('comment/post/(?P<post_pk>[0-9]+)/', CommentView.as_view(), name='post_comment'),
]