from django import template
from djangoonlinestore import settings

register = template.Library()


@register.filter()
def mediapath(image):
    media_url = settings.MEDIA_URL

    return f'{media_url}{image}'
