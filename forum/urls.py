from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path("",                     views.index,          name="index"),
    path("<slug:forum>/",        views.TopicList.as_view(), name="board"),
    path("<slug:forum>/<int:pk>-<slug:slug>/",
         views.TopicDetail.as_view(),                name="topic"),
]
