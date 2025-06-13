from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Category, Product

def home(request):
    """
    Представление для главной страницы
    """
    products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'title': _('Главная')
    }
    return render(request, 'shop/home.html', context)

def catalog(request):
    """
    Представление для страницы каталога товаров
    """
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')
    
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'search_query': search_query,
        'title': _('Каталог')
    }
    return render(request, 'shop/catalog.html', context)

def product_detail(request, slug):
    """
    Представление для страницы отдельного товара
    """
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
        'title': product.name
    }
    return render(request, 'shop/product_detail.html', context)

def about(request):
    """
    Представление для страницы о нас
    """
    return render(request, 'shop/about.html', {'title': _('О нас')})

def contact(request):
    """
    Представление для страницы контактов
    """
    return render(request, 'shop/contact.html', {'title': _('Контакты')})
