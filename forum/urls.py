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

from django.urls import path
from . import views

app_name = "forum"

# URLS for the forum
urlpatterns = [
    path("",                     views.index,          name="index"),
    path("<slug:forum>/",        views.TopicList.as_view(), name="board"),
    path("<slug:forum>/new/",       views.new_topic,   name="topic_new"),
    path("reply/<int:topic_id>/",   views.reply_post,  name="reply"),
    path("<slug:forum>/<int:pk>-<slug:slug>/",
         views.TopicDetail.as_view(),                name="topic"),
    path("post/<int:pk>/edit/", views.PostUpdate.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PostDelete.as_view(), name="post_delete"),
]
