from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, OrderItem

@login_required
def add_to_cart(request, product_id):
    """
    Представление для добавления товара в корзину
    """
    product = get_object_or_404(Product, id=product_id, available=True)
    quantity = int(request.POST.get('quantity', 1))
    
    # Получаем или создаем активную корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    
    # Проверяем, есть ли уже такой товар в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    
    messages.success(request, _('Товар добавлен в корзину!'))
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    """
    Представление для удаления товара из корзины
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, _('Товар удален из корзины!'))
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    """
    Представление для обновления количества товара в корзине
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    messages.success(request, _('Корзина обновлена!'))
    return redirect('cart')

@login_required
def cart(request):
    """
    Представление для просмотра корзины
    """
    try:
        cart = Cart.objects.get(user=request.user, active=True)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'title': _('Корзина')
    }
    return render(request, 'shop/cart.html', context)

@login_required
def checkout(request):
    """
    Представление для оформления заказа
    """
    try:
        cart = Cart.objects.get(user=request.user, active=True)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        messages.error(request, _('Ваша корзина пуста!'))
        return redirect('cart')
    
    if not cart_items:
        messages.error(request, _('Ваша корзина пуста!'))
        return redirect('cart')
    
    if request.method == 'POST':
        # Создаем заказ
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            note=request.POST.get('note', '')
        )
        
        # Добавляем товары из корзины в заказ
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
        
        # Деактивируем корзину
        cart.active = False
        cart.save()
        
        messages.success(request, _('Ваш заказ успешно оформлен!'))
        return redirect('order_confirmation', order_id=order.id)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'user': request.user,
        'title': _('Оформление заказа')
    }
    return render(request, 'shop/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    """
    Представление для подтверждения заказа
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
        'title': _('Подтверждение заказа')
    }
    return render(request, 'shop/order_confirmation.html', context)
