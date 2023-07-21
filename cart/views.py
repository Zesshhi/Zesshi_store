from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Posts
from store.views import docs_info
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect


@require_POST
def cart_add(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Posts, id=post_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(post=post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Posts, id=post_id)
    cart.remove(post=post)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart, })


def cart_payment(request):
    return redirect(docs_info)
