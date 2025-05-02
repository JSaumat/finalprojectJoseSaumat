from django.contrib import admin
from .models import Category, Forum, Topic, Post

# Category class for top level display
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "position")     # Shows sortable position column

# Forum board class inside a category
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "topic_count", "post_count", "position")

    list_filter  = ("category",)        # Sidebar filter by category

    prepopulated_fields = {"slug": ("name",)}       # Auto slug generation

# Inline showing posts inside the Topic admin
class PostInline(admin.TabularInline):

    model = Post

    extra = 0       # No empty rows by default

    readonly_fields = ("author", "created_at")

# Topic thread admin
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = ("title", "forum", "starter", "reply_count",
                    "pinned", "locked", "updated_at")

    list_filter  = ("forum", "pinned", "locked")

    prepopulated_fields = {"slug": ("title",)}

    inlines = (PostInline,)     # Shows posts inline on topic page

# Post for individual message admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("topic", "author", "created_at")

    list_filter  = ("topic__forum", "author")

    search_fields = ("message",)        # Full-text search inside a message
