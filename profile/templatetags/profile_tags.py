from django                     import template
from django.template            import resolve_variable, NodeList

register = template.Library()

@register.tag()
def rating_stars(value, arg):

    stars = ""

    for c in range(0, count):
        stars = stars + "<span class=\"glyphicon glyphicon-star\"></span>"

    remaining_stars = 5 - count

    if remaining_stars != 0:

        for c in range(0, remaining_stars):
            stars = stars + "<span class=\"glyphicon glyphicon-star-empty\"></span>"

    return stars
