

from django.contrib import admin
from .models import Article, ViewSite

@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['id', 'title', 'author', 'content', 'image', 'views', 'date_created']


@admin.register(ViewSite)
class ProductAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['id', 'hostname', 'ip_address']



