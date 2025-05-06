'''

INF601 - Programming in Python

Assignment:  Final Project

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

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
