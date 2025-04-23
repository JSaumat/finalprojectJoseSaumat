from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Category, Forum, Topic
from django.db.models import F

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
