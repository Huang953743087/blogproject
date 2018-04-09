from django.db import models

class Comment(models.Model):
    name=models.CharField(max_length=100, verbose_name=u'题目')
    email=models.EmailField(max_length=255, verbose_name=u'留言邮箱')
    url=models.URLField(blank=True)
    text = models.TextField(verbose_name=u'留言内容')
    created_time=models.DateTimeField(auto_now_add=True,)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, verbose_name=u'文章')
    def __str__(self):
        return self.text[:20]
