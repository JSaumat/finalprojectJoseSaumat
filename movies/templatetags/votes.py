from django import template
register = template.Library()

@register.simple_tag
def user_vote(movie, user):
    return movie.user_vote(user)
