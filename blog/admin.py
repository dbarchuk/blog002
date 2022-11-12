from django.contrib import admin

from .models import Post, Comment, Image, Tag


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 1


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, CommentInLine]
    filter_horizontal = ["tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
