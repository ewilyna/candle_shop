"""
Контекстные процессоры для интернет-магазина ароматических свечей.
Предоставляют доступ к корзине пользователя во всех шаблонах.
"""

from .models import Cart

def cart(request):
    """
    Контекстный процессор для доступа к корзине пользователя.
    Возвращает количество товаров в корзине для отображения в шапке сайта.
    
    Args:
        request: HTTP-запрос
        
    Returns:
        dict: Словарь с количеством товаров в корзине
    """
    cart_count = 0
    
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user, active=True)
            cart_count = sum(item.quantity for item in user_cart.items.all())
        except Cart.DoesNotExist:
            cart_count = 0
    
    return {'cart_count': cart_count}
