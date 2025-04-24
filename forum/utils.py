from .models import Post


def bump_counters(post: Post):
    """
    Recalculate reply_count, view_count, post_count, and last-post pointers
    after inserting a new Post.
    """
    topic = post.topic
    forum = topic.forum

    topic.reply_count = topic.posts.count() - 1
    topic.updated_at  = post.created_at
    topic.save(update_fields=["reply_count", "updated_at"])

    forum.topic_count = forum.topics.count()
    forum.post_count  = Post.objects.filter(topic__forum=forum).count()
    forum.last_post   = post
    forum.save(update_fields=["topic_count", "post_count", "last_post"])
