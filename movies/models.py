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

    # Media type choices
    MOVIE = "movie"
    TV = "tv"
    MEDIA_CHOICES = (
        (MOVIE, "Movie"),
        (TV, "TV Show"),
    )

    media_type = models.CharField(
        max_length=5,                   # fits the words movie and TV
        choices=MEDIA_CHOICES,
        default=MOVIE,
        db_index=True,                  # Helps with faster filtering
    )

    # Basic data below

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

    # Total number of votes cast by the members of the site before the net-like refactor
    # vote_count = models.IntegerField(default=0)

    # Helps Django to enforce uniqueness
    class Meta:

        unique_together = ("tmdb_id", "media_type")  # one vote per user per movie
        verbose_name = "Media content"  # label in the change form
        verbose_name_plural = "Media content"  # label in the sidebar

    # Defines how the object (movie or tv show) appears
    def __str__(self):

        return f"{self.title} ({self.get_media_type_display()})"

    # Keeps track of net-likes that appear next to the like button
    @property
    def likes(self):

        """
        Net likes: +1 for each like vote, −1 for each dislike vote.
        Ex. 3 likes, 2 dislikes ⇒ 3 - 2 = 1 net Like
        """

        plus = self.votes.filter(value=MovieVote.LIKE).count()

        minus = self.votes.filter(value=MovieVote.DISLIKE).count()

        return plus - minus

    # Keeps track of dislikes that appear next to the dislike button
    @property
    def dislikes(self):

        return self.votes.filter(value=MovieVote.DISLIKE).count()

    # Keeps track of user votes
    def user_vote(self, user):

        """
                Helper: return current user’s vote on this movie
                •  1  → user liked
                • -1  → user disliked
                •  0  → no vote or user not authenticated
                """

        if not user.is_authenticated:

            return 0

        obj = self.votes.filter(user=user).first()

        return obj.value if obj else 0

    # new helpers
    @property
    def likes_raw(self):
        """How many users currently have 👍 on this title."""
        return self.votes.filter(value=MovieVote.LIKE).count()

    @property
    def dislikes_raw(self):
        """How many users currently have 👎 on this title."""
        return self.votes.filter(value=MovieVote.DISLIKE).count()

    # Helps Django to enforce uniqueness (Duplicate)
    # class Meta:
    #
    #     unique_together = ("tmdb_id", "media_type")  # one vote per user per movie

#Improved movie voting class
class MovieVote(models.Model):

    """
        One row per user’s vote on a Movie.

        value:
            1  → like
           -1  → dislike
        The (user, movie) pair is unique to enforce “one vote per user”.
        """

    LIKE, DISLIKE = 1, -1
    VOTE_CHOICES = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )

    # Tracks who cast the vote
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Tracks what the user voted on
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="votes")

    # Tracks like or dislike
    value = models.SmallIntegerField(choices=VOTE_CHOICES)