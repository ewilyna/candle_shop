from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    """
    Модель категории товаров
    """
    name = models.CharField(_('Название'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    description = models.TextField(_('Описание'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Модель товара (ароматической свечи)
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name=_('Категория'))
    name = models.CharField(_('Название'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    image = models.ImageField(_('Изображение'), upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(_('Описание'))
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_('Наличие на складе'), default=0)
    available = models.BooleanField(_('Доступен'), default=True)
    created = models.DateTimeField(_('Создан'), auto_now_add=True)
    updated = models.DateTimeField(_('Обновлен'), auto_now=True)
    aroma = models.CharField(_('Аромат'), max_length=100)
    burn_time = models.PositiveIntegerField(_('Время горения (часов)'), default=0)
    weight = models.DecimalField(_('Вес (г)'), max_digits=6, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return f'/product/{self.slug}/'

class Cart(models.Model):
    """
    Модель корзины покупок
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts', verbose_name=_('Пользователь'))
    created = models.DateTimeField(_('Создана'), auto_now_add=True)
    updated = models.DateTimeField(_('Обновлена'), auto_now=True)
    active = models.BooleanField(_('Активна'), default=True)
    
    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')
        
    def __str__(self):
        return f'Корзина {self.user.username}'
        
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class CartItem(models.Model):
    """
    Модель элемента корзины
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name=_('Корзина'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', verbose_name=_('Товар'))
    quantity = models.PositiveIntegerField(_('Количество'), default=1)
    
    class Meta:
        verbose_name = _('Элемент корзины')
        verbose_name_plural = _('Элементы корзины')
        
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
        
    def get_cost(self):
        return self.product.price * self.quantity

class Order(models.Model):
    """
    Модель заказа
    """
    STATUS_CHOICES = (
        ('new', _('Новый')),
        ('processing', _('В обработке')),
        ('shipped', _('Отправлен')),
        ('delivered', _('Доставлен')),
        ('canceled', _('Отменен')),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name=_('Пользователь'))
    first_name = models.CharField(_('Имя'), max_length=50)
    last_name = models.CharField(_('Фамилия'), max_length=50)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=15)
    address = models.TextField(_('Адрес доставки'))
    created = models.DateTimeField(_('Создан'), auto_now_add=True)
    updated = models.DateTimeField(_('Обновлен'), auto_now=True)
    status = models.CharField(_('Статус'), max_length=20, choices=STATUS_CHOICES, default='new')
    note = models.TextField(_('Примечание'), blank=True)
    
    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        ordering = ['-created']
        
    def __str__(self):
        return f'Заказ {self.id}'
        
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    """
    Модель элемента заказа
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Заказ'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Товар'))
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('Количество'), default=1)
    
    class Meta:
        verbose_name = _('Элемент заказа')
        verbose_name_plural = _('Элементы заказа')
        
    def __str__(self):
        return f'{self.id}'
        
    def get_cost(self):
        return self.price * self.quantity
