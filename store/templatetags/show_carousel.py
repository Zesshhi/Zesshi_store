from django import template

from store.models import Carousel

register = template.Library()


@register.inclusion_tag('inc/_carousel.html')
def show_carousel():
    carousel = Carousel.objects.all()
    return {'carousel': carousel}
