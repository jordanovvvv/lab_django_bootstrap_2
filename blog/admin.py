from django.contrib import admin
from django.shortcuts import get_object_or_404, render

from .forms import CommentForm
from .models import BlogPost, BlogComment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', )
    search_fields = ['title', 'content']

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['author', 'content']
    actions = ['approve_comments']

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(BlogPost, PostAdmin)

