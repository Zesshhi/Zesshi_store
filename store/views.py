import csv
import datetime

from .models import *
from cart.cart import *
from .forms import UserRegisterForm, UserLoginForm, ContactForm, OrderCreateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from cart.forms import CartAddProductForm


class Home(ListView):
    model = Posts
    template_name = 'store/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm
        return context

    def get_queryset(self):
        return Posts.objects.filter(available=True)


class GetPost(DetailView):
    model = Posts
    template_name = 'store/main_pages/single_page.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['form'] = CartAddProductForm
        return context


class PostByGenre(ListView):
    template_name = 'store/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Posts.objects.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Playstation Store'
        return context


class Search(ListView):
    template_name = 'store/search.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Posts.objects.filter(title__icontains=self.request.GET.get('search')).prefetch_related('genre')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f'search={self.request.GET.get("search")}&'
        return context


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'store/auth/register.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'store/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'nightmarious@mail.ru',
                             ['shalltear_ziegler@mail.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
                return redirect('contact')
        else:
            messages.error(request, 'Ошибка отправки')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'store/main_pages/contact_us.html', {'form': form})


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['post'], price=item['price'])

            cart.clear()
            return render(request, 'store/orders/created.html', {'order': order})
    else:
        if request.user.is_authenticated:
            initial = {
                'username': request.user.username,
                'email': request.user.email
            }
        else:
            initial = {}
        form = OrderCreateForm(initial=initial)

    return render(request, 'store/orders/create.html', {'cart': cart, 'form': form})



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


def docs_info(request):
    return render(request, 'store/docs_info/docs_info.html')


def docs_agreement(request):
    return render(request, 'store/docs_info/agreement.html')


def docs_personal(request):
    return render(request, 'store/docs_info/personal_data.html')


def docs_privacy(request):
    return render(request, 'store/docs_info/privacy.html')


@login_required
def profile(request):
    user_main_orders = Order.objects.filter(username=request.user.username)


    data = {
        'user_main_orders': user_main_orders,
    }
    return render(request, 'store/main_pages/profile.html', data)



