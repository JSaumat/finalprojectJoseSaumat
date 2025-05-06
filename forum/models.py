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
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()         # Custom auth user model

# Class for categories in the forum
class Category(models.Model):

    name        = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=255, blank=True)
    position    = models.PositiveSmallIntegerField(default=0)       # A manual sort

    class Meta:

        ordering = ("position",)

    def __str__(self):

        return self.name

# The board inside a category
class Forum(models.Model):

    category    = models.ForeignKey(Category, related_name="forums", on_delete=models.CASCADE)
    name        = models.CharField(max_length=80)
    slug        = models.SlugField(max_length=90, unique=True, blank=True)
    blurb       = models.CharField(max_length=255, blank=True)
    position    = models.PositiveSmallIntegerField(default=0)

    # Counters for quick display
    topic_count = models.PositiveIntegerField(default=0)
    post_count  = models.PositiveIntegerField(default=0)

    # Points to most recent post
    last_post = models.ForeignKey(

        "Post", null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+"

    )

    class Meta:
        ordering = ("position",)

    # Auto-generates slug once
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Topic thread inside a forum
class Topic(models.Model):

    forum       = models.ForeignKey(Forum, related_name="topics", on_delete=models.CASCADE)
    title       = models.CharField(max_length=140)
    slug        = models.SlugField(max_length=150, blank=True)
    starter     = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(default=timezone.now)
    view_count  = models.PositiveIntegerField(default=0)
    reply_count = models.PositiveIntegerField(default=0)
    pinned      = models.BooleanField(default=False)
    locked      = models.BooleanField(default=False)

    class Meta:
        ordering = ("-pinned", "-updated_at")       # Pinned first, then the newest

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title

# Post message inside a topic
class Post(models.Model):

    topic       = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    message     = models.TextField(max_length=10_000)
    created_at  = models.DateTimeField(default=timezone.now)
    edited_at   = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("created_at",)      # Chronological order inside a topic

    def __str__(self):

        # Provides a preview of the first 40 characters
        return f"{self.author}: {self.message[:40]}"
