from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Административная панель для управления категориями товаров
    """
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для управления товарами
    """
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'aroma')
    date_hierarchy = 'created'
    ordering = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Административная панель для управления корзинами
    """
    list_display = ('user', 'created', 'updated', 'active')
    list_filter = ('active', 'created')
    search_fields = ('user__username',)
    date_hierarchy = 'created'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Административная панель для управления элементами корзины
    """
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart__active',)
    search_fields = ('cart__user__username', 'product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Административная панель для управления заказами
    """
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    date_hierarchy = 'created'
    ordering = ('-created',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Административная панель для управления элементами заказа
    """
    list_display = ('order', 'product', 'price', 'quantity')
    list_filter = ('order__status',)
    search_fields = ('order__user__username', 'product__name')
