from django.contrib import admin

from apps.blog.models import Quote, BlogPost, BlogPostImage, BlogPostComment
from apps.courses.models import Category


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPostImage)
class BlogPostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPostComment)
class BlogPostCommentAdmin(admin.ModelAdmin):
    pass
