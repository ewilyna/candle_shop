from django.urls import path
from . import views
from . import cart_views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Корзина и заказы
    path('cart/', cart_views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', cart_views.update_cart, name='update_cart'),
    path('checkout/', cart_views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', cart_views.order_confirmation, name='order_confirmation'),
]
