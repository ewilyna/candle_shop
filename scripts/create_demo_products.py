#!/usr/bin/env python
"""
Скрипт для загрузки демонстрационных товаров в базу данных
"""
import os
import sys
import django

# Настройка окружения Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'candle_shop.settings')
django.setup()

# Импорт моделей
from shop.models import Category, Product

def create_demo_products():
    """
    Создает демонстрационные категории и товары
    """
    # Создание категорий
    categories = [
        {
            'name': 'Классические свечи',
            'slug': 'classic-candles',
            'description': 'Традиционные ароматические свечи в стеклянных сосудах'
        },
        {
            'name': 'Соевые свечи',
            'slug': 'soy-candles',
            'description': 'Экологичные свечи из натурального соевого воска'
        },
        {
            'name': 'Подарочные наборы',
            'slug': 'gift-sets',
            'description': 'Наборы ароматических свечей для подарка'
        }
    ]
    
    category_objects = {}
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={
                'name': cat_data['name'],
                'description': cat_data['description']
            }
        )
        category_objects[cat_data['slug']] = category
        if created:
            print(f"Создана категория: {category.name}")
        else:
            print(f"Категория уже существует: {category.name}")
    
    # Создание товаров
    products = [
        {
            'category': 'classic-candles',
            'name': 'Лавандовый сад',
            'slug': 'lavender-garden',
            'description': 'Успокаивающий аромат лаванды поможет расслабиться после тяжелого дня и создаст атмосферу уюта в вашем доме. Свеча изготовлена из натурального воска с добавлением эфирного масла лаванды.',
            'price': 890.00,
            'stock': 25,
            'aroma': 'Лаванда',
            'burn_time': 40,
            'weight': 250.00
        },
        {
            'category': 'classic-candles',
            'name': 'Ванильное облако',
            'slug': 'vanilla-cloud',
            'description': 'Теплый и сладкий аромат ванили создаст уютную атмосферу в любом помещении. Идеально подходит для гостиной или спальни. Свеча изготовлена из высококачественного воска с натуральными ароматизаторами.',
            'price': 750.00,
            'stock': 30,
            'aroma': 'Ваниль',
            'burn_time': 35,
            'weight': 220.00
        },
        {
            'category': 'soy-candles',
            'name': 'Морской бриз',
            'slug': 'sea-breeze',
            'description': 'Свежий аромат морского бриза перенесет вас на побережье океана. Свеча изготовлена из экологически чистого соевого воска, который горит дольше и не выделяет вредных веществ.',
            'price': 950.00,
            'stock': 20,
            'aroma': 'Морской бриз',
            'burn_time': 45,
            'weight': 280.00
        },
        {
            'category': 'soy-candles',
            'name': 'Цитрусовый микс',
            'slug': 'citrus-mix',
            'description': 'Бодрящий аромат цитрусовых фруктов наполнит ваш дом энергией и свежестью. Идеально подходит для кухни или рабочего кабинета. Свеча изготовлена из натурального соевого воска с добавлением эфирных масел апельсина, лимона и грейпфрута.',
            'price': 850.00,
            'stock': 15,
            'aroma': 'Цитрусовые',
            'burn_time': 38,
            'weight': 240.00
        },
        {
            'category': 'gift-sets',
            'name': 'Набор "Времена года"',
            'slug': 'seasons-set',
            'description': 'Подарочный набор из 4 свечей, каждая из которых отражает аромат определенного времени года: весенние цветы, летний сад, осенний лес и зимняя хвоя. Идеальный подарок для любого случая.',
            'price': 2500.00,
            'stock': 10,
            'aroma': 'Ассорти',
            'burn_time': 120,
            'weight': 600.00
        },
        {
            'category': 'gift-sets',
            'name': 'Набор "Спа-день"',
            'slug': 'spa-day-set',
            'description': 'Набор из 3 свечей с расслабляющими ароматами для создания атмосферы спа у вас дома. В набор входят свечи с ароматами лаванды, эвкалипта и иланг-иланга. Идеально подходит для ванной комнаты или спальни.',
            'price': 1800.00,
            'stock': 12,
            'aroma': 'Спа-ароматы',
            'burn_time': 90,
            'weight': 450.00
        }
    ]
    
    for prod_data in products:
        product, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults={
                'category': category_objects[prod_data['category']],
                'name': prod_data['name'],
                'description': prod_data['description'],
                'price': prod_data['price'],
                'stock': prod_data['stock'],
                'available': True,
                'aroma': prod_data['aroma'],
                'burn_time': prod_data['burn_time'],
                'weight': prod_data['weight']
            }
        )
        if created:
            print(f"Создан товар: {product.name}")
        else:
            print(f"Товар уже существует: {product.name}")

if __name__ == '__main__':
    print("Начало создания демонстрационных товаров...")
    create_demo_products()
    print("Демонстрационные товары успешно созданы!")
