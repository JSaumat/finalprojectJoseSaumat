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

from .models import Post


def bump_counters(post: Post):
    """
    Recalculate reply_count, view_count, post_count, and last-post pointers
    after inserting a new Post.
    """
    topic = post.topic      # Thread the post belongs to
    forum = topic.forum     # Board the thread belongs to

    # Topic‑level counters
    # reply_count excludes the first post (hence −1)
    topic.reply_count = topic.posts.count() - 1
    topic.updated_at  = post.created_at     # bumps "last activity" timestamp
    topic.save(update_fields=["reply_count", "updated_at"])

    # Forum‑level counters
    forum.topic_count = forum.topics.count()        # Total threads
    forum.post_count  = Post.objects.filter(topic__forum=forum).count()
    forum.last_post   = post                        # Newest overall
    forum.save(update_fields=["topic_count", "post_count", "last_post"])
