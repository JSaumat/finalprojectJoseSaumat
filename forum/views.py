from django.shortcuts import (get_object_or_404, render)
from django.views.generic import ListView, DetailView
from .models import Category, Forum, Topic
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from .forms import NewTopicForm, PostForm
from .utils import bump_counters
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from .models import Post
from django.utils import timezone


def index(request):
    cats = Category.objects.prefetch_related("forums")
    return render(request, "forum/index.html", {"cats": cats})

class TopicList(ListView):
    paginate_by = 25
    template_name = "forum/board.html"
    context_object_name = "topics"

    def get_queryset(self):
        self.board = get_object_or_404(Forum, slug=self.kwargs["forum"])
        return self.board.topics.select_related("starter")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["board"] = self.board
        return ctx

class TopicDetail(DetailView):
    model = Topic
    template_name = "forum/topic.html"
    pk_url_kwarg  = "pk"

    def get_object(self):
        obj = super().get_object()
        Topic.objects.filter(pk=obj.pk).update(view_count=F("view_count") + 1)
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["post_form"] = PostForm()  # inject a blank form
        return ctx

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = "forum/post_edit.html"

    def test_func(self):
        """Only allow the author or staff to edit."""
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.edited_at = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        post  = self.get_object()
        topic = post.topic
        return reverse(
            "forum:topic",
            kwargs={
                "forum": topic.forum.slug,
                "pk":    topic.pk,
                "slug":  topic.slug,
            }
        )

@login_required
def new_topic(request, forum):
    """Create first post + topic."""
    board = get_object_or_404(Forum, slug=forum)

    if request.method == "POST":
        t_form = NewTopicForm(request.POST)
        p_form = PostForm(request.POST)
        if t_form.is_valid() and p_form.is_valid():
            topic           = t_form.save(commit=False)
            topic.forum     = board
            topic.starter   = request.user
            topic.save()

            post            = p_form.save(commit=False)
            post.topic      = topic
            post.author     = request.user
            post.save()

            bump_counters(post)
            return redirect("forum:topic", forum=board.slug,
                            pk=topic.pk, slug=topic.slug)
    else:
        t_form, p_form = NewTopicForm(), PostForm()

    return render(request, "forum/topic_new.html",
                  {"board": board, "t_form": t_form, "p_form": p_form})


@login_required
def reply_post(request, topic_id):
    """Handle POST for a reply inside a topic."""
    topic = get_object_or_404(Topic, pk=topic_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            reply          = form.save(commit=False)
            reply.topic    = topic
            reply.author   = request.user
            reply.save()
            bump_counters(reply)
            return redirect(
                "forum:topic",
                forum=topic.forum.slug, pk=topic.pk, slug=topic.slug
            )
    # Fallback: go back to topic view even if invalid
    return redirect("forum:topic", forum=topic.forum.slug,
                    pk=topic.pk, slug=topic.slug)