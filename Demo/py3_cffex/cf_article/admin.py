from django.contrib import admin
from .models import *


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title']


class PostInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'post_date', 'post_date_gmt', 'post_author', 'post_excerpt', 'post_parent', 'post_status', 'post_content_filtered']

admin.site.register(PostInfo, PostInfoAdmin)
admin.site.register(TypeInfo, TypeInfoAdmin)
