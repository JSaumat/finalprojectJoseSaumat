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

from .models import Movie

# Change admin site headers
admin.site.site_header = "Sam's Picks Admin"

admin.site.site_title = "Sam's Picks Admin Portal"

admin.site.index_title = "Welcome to the Sam's Picks Management Area"

# Register your models here.
# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#
#     list_display = ('title', 'release_date', 'vote_count')
#
#     search_fields = ('title',)

# Controls the information visible in the /admin page
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    """
        Custom admin for the Movie / TV‑show model.

        * list_display — columns visible in the changelist:
            • title        – movie / show title
            • media_type   – "movie" or "tv"
            • likes_raw    – raw like count   (property on the model)
            • dislikes_raw – raw dislike count
            • net_likes    – computed below = likes − dislikes
        """


    list_display = ("title", "media_type", "likes_raw", "dislikes_raw", "net_likes")

    def net_likes(self, obj):
        return obj.likes        # positive, negative, or zero likes

    # Column header text
    net_likes.short_description = "Net Likes"