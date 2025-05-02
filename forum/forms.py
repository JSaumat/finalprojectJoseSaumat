from django import forms
from .models import Topic, Post

# Collects thread title
class NewTopicForm(forms.ModelForm):

    class Meta:

        model  = Topic

        fields = ("title",)     # Only expose the title field

# Collects a post or reply message
class PostForm(forms.ModelForm):

    class Meta:

        model  = Post

        fields = ("message",)

        # Uses a multi-line widget for the message body
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
