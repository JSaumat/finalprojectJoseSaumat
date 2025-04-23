from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()

class Category(models.Model):
    name        = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=255, blank=True)
    position    = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("position",)

    def __str__(self):
        return self.name


class Forum(models.Model):
    category    = models.ForeignKey(Category, related_name="forums",
                                    on_delete=models.CASCADE)
    name        = models.CharField(max_length=80)
    slug        = models.SlugField(max_length=90, unique=True, blank=True)
    blurb       = models.CharField(max_length=255, blank=True)
    position    = models.PositiveSmallIntegerField(default=0)
    topic_count = models.PositiveIntegerField(default=0)
    post_count  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("position",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Topic(models.Model):
    forum       = models.ForeignKey(Forum, related_name="topics",
                                    on_delete=models.CASCADE)
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
        ordering = ("-pinned", "-updated_at")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    topic       = models.ForeignKey(Topic, related_name="posts",
                                    on_delete=models.CASCADE)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    message     = models.TextField(max_length=10_000)
    created_at  = models.DateTimeField(default=timezone.now)
    edited_at   = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.author}: {self.message[:40]}"
