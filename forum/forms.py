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
