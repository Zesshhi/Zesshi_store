from django import template

from store.models import Genre

register = template.Library()


@register.inclusion_tag('store/lists/list_of_genres.html')
def show_genres():
    genre = Genre.objects.all()
    return {'genre': genre}