from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *
from .views import export_to_csv


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PlatformAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'price', 'get_photo', 'available', 'version_of_platform',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('genre', 'platform')
    readonly_fields = ('views', 'get_photo')
    fields = ('title', 'slug', 'genre', 'platform', 'available', 'description', 'content', 'release_date', 'price',
              'photo',
              'get_photo', 'views',
              'version_of_platform')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class CarouselAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'get_photo')
    search_fields = ('title',)
    readonly_fields = ('get_photo',)
    field = ('title', 'slug', 'photo', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        return '-'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'vk_or_telegram',
                    'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Genre, GenreAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Order, OrderAdmin)
