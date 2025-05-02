from django import template

register = template.Library()       # Django’s tag/filters registry

# Custom template tag for user voting
@register.simple_tag
def user_vote(movie, user):
    return movie.user_vote(user)
