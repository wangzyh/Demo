# coding:utf-8
from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    post_title = models.CharField(max_length=100)
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=20)


    def __str__(self):
        return self.ttitle.encode('utf-8')

class PostInfo(models.Model):

    post_date = models.DateTimeField()
    # 格林威治时间
    post_date_gmt = models.DateField()             
    post_author = models.CharField(max_length=20)
    # 摘抄
    post_excerpt = HTMLField()                  
    post_parent = models.CharField(max_length=40)
    post_status = models.BooleanField()
    menu_order = models.CharField(max_length=20)

   # 更改时间
    post_modified = models.DateTimeField()             
    post_modified_gmt = models.TimeField()     
    # 内容过滤     
    post_content_filtered = models.BooleanField()   

    guid = models.CharField(max_length=128)

    # 评论状态
    comment_status = models.CharField(max_length=2)
    comment_count = models.IntegerField()

    to_ping = models.BooleanField()
    pinged = models.BooleanField()
    ping_status = models.BooleanField()

