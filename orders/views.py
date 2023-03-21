from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import *


def create_order(request):
    products = Product.objects.all()
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        order_products = []
        for product in products:
            quantity = request.POST.get(f'product_{product.id}')
            if quantity:
                order_products.append(OrderProduct(product=product, quantity=quantity))
        order = Order.objects.create(person_name=person_name)
        order.products.set(order_products)
    context = {
        'products': products
    }
    return render(request, 'create_order.html', context)


def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'order_list.html', context)


def order_progress(request):
    orders = Order.objects.annotate(total_time_to_cook=Sum('orderproduct__product__time_to_cook'))
    context = {
        'orders': orders
    }
    return render(request, 'order_progress.html', context)
