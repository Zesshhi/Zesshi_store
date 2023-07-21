from django import template
from store.models import Posts

register = template.Library()


@register.inclusion_tag('store/lists/popular_posts_tpl.html')
def get_popular_posts(cnt=3):
    posts = Posts.objects.order_by('-views')[:cnt]
    return {'posts': posts}

