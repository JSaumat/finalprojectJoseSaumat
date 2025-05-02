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

from django.db import models
from django.conf import settings
from django.db.models import Count, Q

# Create your models here.

# Movie model represents each movie record saved in the database
class Movie(models.Model):

    MOVIE = "movie"
    TV = "tv"
    MEDIA_CHOICES = (
        (MOVIE, "Movie"),
        (TV, "TV Show"),
    )

    media_type = models.CharField(
        max_length=5,
        choices=MEDIA_CHOICES,
        default=MOVIE,
        db_index=True,
    )

    # Movie title
    title = models.CharField(max_length=200)

    # TMDB's unique ID for each movie
    tmdb_id = models.IntegerField()

    # Link to movies movie poster if available
    poster_url = models.URLField(blank=True)

    # Link to movie description
    description = models.TextField(blank=True)

    # Link to movie release date
    release_date = models.DateField(null=True, blank=True)

    # Total number of votes cast by the members of the site
    vote_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ("tmdb_id", "media_type")  # one vote per user per movie

    # Defines how the object appears
    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"

    @property
    def likes(self):
        """
        Net likes: +1 for each like vote, −1 for each dislike vote.
        E.g. 3 likes, 2 dislikes ⇒ 1
        """
        plus = self.votes.filter(value=MovieVote.LIKE).count()
        minus = self.votes.filter(value=MovieVote.DISLIKE).count()
        return plus - minus

    @property
    def dislikes(self):
        return self.votes.filter(value=MovieVote.DISLIKE).count()

    def user_vote(self, user):
        if not user.is_authenticated:
            return 0
        obj = self.votes.filter(user=user).first()
        return obj.value if obj else 0

    class Meta:
        unique_together = ("tmdb_id", "media_type")  # one vote per user per movie

#Improved movie voting class
class MovieVote(models.Model):
    LIKE, DISLIKE = 1, -1
    VOTE_CHOICES = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie",
                              on_delete=models.CASCADE,
                              related_name="votes")
    value = models.SmallIntegerField(choices=VOTE_CHOICES)