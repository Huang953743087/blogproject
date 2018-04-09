#!usr/bin/python3
#-*-coding:utf-8-*-

import markdown
from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Post, Category, Tag
from comments.forms import CommentForm


# 首页
class IndexView(View):
    def get(self, request):
            post_list = Post.objects.all().order_by('-created_time')
            return render(request, 'index.html', {'post_list': post_list})


# 文章详情页
class DetailView(View):
    def get(self, request, pk):
        active = Post.objects.get(pk=pk)
        active.click_number+=1
        active.save()
        active.body = markdown.markdown(active.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
        form = CommentForm()
        comment_list=active.comment_set.all()
        return render(request, 'detail.html', {
            'post': active,
            'form': form,
            'comment_list': comment_list,
        })


# 按日期归档
class ArchiveView(View):
    def get(self, request, year, month):
        post_list = Post.objects.filter(created_time__year=year,
                                        created_time__month=month
                                        ).order_by('-created_time')
        return render(request, 'index.html', context={'post_list': post_list})


# 按分类查找
class CategoryView(View):
    def get(self, request, pk):
        Cate = Category.objects.get(pk=pk)
        post_list=Cate.post_set.all().order_by('-created_time')
        return render(request, 'index.html', context={'post_list': post_list})


# 按标签查找
class TagView(View):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        post_list = tag.post_set.all().order_by('-created_time')
        return render(request, 'index.html', context={'post_list': post_list})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class ConnectView(View):
    def get(self, request):
        return render(request, 'connect.html', {})