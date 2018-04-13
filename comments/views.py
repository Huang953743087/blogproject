from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Post
from comments.forms import CommentForm


class CommentView(View):
    def post(self, request, post_pk):
        # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
        # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
        # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户
        # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
        # 因此只有当用户的请求为 post 时才需要处理表单数据。
        active=Post.objects.get(pk=post_pk)
        form=CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            comment=form.save(commit=False)
            # 将评论和被评论的文章关联起来。
            comment.post=active
            comment.save()
            comment_list = active.comment_set.all()
            context = {'post': active,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'detail.html', context=context)
        else:
                '''
                检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
                因此我们传了三个模板变量给 detail.html，
                一个是文章（Post），一个是评论列表，一个是表单 form
                注意这里我们用到了 post.comment_set.all() 方法，
                这个用法有点类似于 Post.objects.all()
                其作用是获取这篇 post 下的的全部评论，
                因为 Post 和 Comment 是 ForeignKey 关联的，
                因此使用 post.comment_set.all() 反向查询全部评论。
                '''
                comment_list = active.comment_set.all()
                context = {'post': active, 'form': form, 'comment_list': comment_list}
                return render(request, 'detail.html', context=context)
