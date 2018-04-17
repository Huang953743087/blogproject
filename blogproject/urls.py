"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from blog.feeds import AllPostsRssFeed
from blog.views import IndexView
from blogproject.settings import STATIC_ROOT

urlpatterns = [
    # 首页
    path('', IndexView.as_view(), name='index'),
    # 管理界面
    path('admin/', admin.site.urls),
    # blog界面
    path('blog/', include('blog.urls', namespace='blog')),
    # 评论界面
    path('comment/', include('comments.urls', namespace='comment')),
    re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
]
