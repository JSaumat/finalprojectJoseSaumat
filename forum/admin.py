from django.contrib import admin
from .models import Category, Forum, Topic, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "position")

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "topic_count", "post_count", "position")
    list_filter  = ("category",)
    prepopulated_fields = {"slug": ("name",)}

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    readonly_fields = ("author", "created_at")

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "forum", "starter", "reply_count",
                    "pinned", "locked", "updated_at")
    list_filter  = ("forum", "pinned", "locked")
    prepopulated_fields = {"slug": ("title",)}
    inlines = (PostInline,)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("topic", "author", "created_at")
    list_filter  = ("topic__forum", "author")
    search_fields = ("message",)
