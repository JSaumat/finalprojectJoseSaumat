'''

INF601 - Programming in Python

Assignment #3:  Mini Project 4

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

from django.db import models

# Create your models here.

# Movie model represents each movie record saved in the database
class Movie(models.Model):

    # Movie title
    title = models.CharField(max_length=200)

    # TMDB's unique ID for each movie
    tmdb_id = models.IntegerField(unique=True)

    # Link to movies movie poster if available
    poster_url = models.URLField(blank=True)

    # Link to movie description
    description = models.TextField(blank=True)

    # Link to movie release date
    release_date = models.DateField(null=True, blank=True)

    # Total number of votes cast by the members of the site
    vote_count = models.IntegerField(default=0)

    # Defines how the object appears
    def __str__(self):
        return self.title