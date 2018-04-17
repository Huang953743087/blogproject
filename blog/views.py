#!usr/bin/python3
#-*-coding:utf-8-*-

import markdown
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from blog.models import Post, Category, Tag
from comments.forms import CommentForm


# 首页
class IndexView(View):
    def get(self, request):
            post_list = Post.objects.all().order_by('-created_time')
            # 分页效果，10个每页
            paginator = Paginator(post_list, 10)
            # 先获取page
            page = request.GET.get('page')
            try:
                posts = paginator.page(page)
            # page数字不为整数时
            except PageNotAnInteger:
                posts = paginator.page(1)
            # page超出了最大数时
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            return render(request, 'index.html', {'post_list': posts})


# 文章详情页
class DetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        # 增加点击数
        post.click_number += 1
        post.save()
        md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                       TocExtension(slugify=slugify),
                                  ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        form = CommentForm()
        comment_list = post.comment_set.all()
        return render(request, 'detail.html', {
            'post': post,
            'form': form,
            'comment_list': comment_list,
        })


# 按日期归档
class ArchiveView(View):
    def get(self, request, year, month):
        post_list = Post.objects.filter(created_time__year=year,
                                        created_time__month=month
                                        ).order_by('-created_time')
        # 分页效果，10个每页
        paginator = Paginator(post_list, 10)
        # 先获取page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        # page数字不为整数时
        except PageNotAnInteger:
            posts = paginator.page(1)
        # page超出了最大数时
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'index.html', context={'post_list': posts})


# 按分类查找
class CategoryView(View):
    def get(self, request, pk):
        Cate = Category.objects.get(pk=pk)
        post_list=Cate.post_set.all().order_by('-created_time')
        # 分页效果，10个每页
        paginator = Paginator(post_list, 10)
        # 先获取page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        # page数字不为整数时
        except PageNotAnInteger:
            posts = paginator.page(1)
        # page超出了最大数时
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'index.html', context={'post_list': posts})


# 按标签查找
class TagView(View):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        post_list = tag.post_set.all().order_by('-created_time')
        # 分页效果，10个每页
        paginator = Paginator(post_list, 10)
        # 先获取page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        # page数字不为整数时
        except PageNotAnInteger:
            posts = paginator.page(1)
        # page超出了最大数时
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'index.html', context={'post_list': posts})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})


class ConnectView(View):
    def get(self, request):
        return render(request, 'connect.html', {})


class SearchView(View):
    def get(self, request):
            q = request.GET.get('q')
            error_msg = ''
            if not q:
                error_msg = "请输入关键词"
                return render(request, 'index.html', {'error_msg': error_msg})
            post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
            return render(request, 'index.html', {'error_msg': error_msg,'post_list': post_list})