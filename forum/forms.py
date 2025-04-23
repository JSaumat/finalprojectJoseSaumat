from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    class Meta:
        model  = Topic
        fields = ("title",)

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ("message",)
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
