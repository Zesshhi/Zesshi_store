from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('search/', Search.as_view(), name='search'),

    path('register/', register, name='register'),

    # path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),

    path('contact_us/', contact_us, name='contact'),

    path('genre/<str:slug>/', PostByGenre.as_view(), name='genre'),


    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('post/<str:slug>/', Genre, name='genre_list'),


    path('cart/create/', order_create, name='order_create'),

    path('docs/info/', docs_info, name='docs_info'),
    path('docs/agreement/', docs_agreement, name='docs_agreement'),
    path('docs/personal_data/', docs_personal, name='docs_personal'),
    path('docs/privacy/', docs_privacy, name='docs_privacy'),


    path('profile/', profile, name='profile'),

]

