from django.urls import path

from .views import *

urlpatterns = [

    path('', cart_detail, name='cart_detail'),
    path('cart/<int:post_id>/', cart_add, name='cart_add'),
    path('cart/<int:post_id>', cart_remove, name='cart_remove'),
    path('cart/payment/', cart_payment, name='cart_payment'),

]