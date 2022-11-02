from django.contrib import admin
from .models import Article,Comment


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['subject']
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)