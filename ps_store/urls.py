from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from two_factor.views import (
    LoginView, ProfileView
)

from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', include('store.urls')),

    path('', include(tf_urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/two_factor/', ProfileView.as_view(), name='profile_two_factor'),

    path('cart/', include('cart.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('adminskaya_zalupa_krota_1x1_zxc_sf/', admin.site.urls),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
