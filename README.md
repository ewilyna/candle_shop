# Инструкция по запуску интернет-магазина "Свечной Дом"

## Требования
- Python 3.8 или выше
- pip (менеджер пакетов Python)

## Установка и запуск

1. **Распакуйте архив** в выбранную директорию

2. **Создайте виртуальное окружение** (если оно не включено в архив):
   ```
   python -m venv venv
   ```

3. **Активируйте виртуальное окружение**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Установите зависимости**:
   ```
   pip install -r requirements.txt
   ```

5. **Выполните миграции базы данных**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Создайте суперпользователя** для доступа к административной панели:
   ```
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки**:
   ```
   python manage.py runserver
   ```

8. **Откройте сайт** в браузере по адресу: `http://127.0.0.1:8000/`

9. **Для доступа к административной панели** перейдите по адресу: `http://127.0.0.1:8000/admin/`

## Структура проекта

- `candle_shop/` - основной пакет проекта Django
  - `settings.py` - настройки проекта
  - `urls.py` - основные URL-маршруты
  - `wsgi.py` и `asgi.py` - файлы для развертывания

- `shop/` - приложение для работы с товарами, каталогом и корзиной
  - `models.py` - модели товаров, категорий, корзины и заказов
  - `views.py` - представления для каталога и товаров
  - `cart_views.py` - представления для корзины и заказов
  - `admin.py` - настройки административной панели
  - `urls.py` - URL-маршруты приложения

- `users/` - приложение для работы с пользователями
  - `models.py` - расширенная модель пользователя
  - `forms.py` - формы для регистрации и профиля
  - `views.py` - представления для регистрации и профиля
  - `urls.py` - URL-маршруты для пользователей

- `templates/` - шаблоны HTML
  - `base/` - базовые шаблоны
  - `shop/` - шаблоны для магазина
  - `users/` - шаблоны для пользователей

- `static/` - статические файлы
  - `css/` - стили CSS
  - `js/` - скрипты JavaScript
  - `images/` - изображения

- `media/` - загружаемые пользователями файлы
  - `products/` - изображения товаров

## Дополнительная информация

- Для добавления товаров и категорий используйте административную панель
- Для тестирования функционала регистрации и заказов создайте тестового пользователя
- Для изменения дизайна отредактируйте файлы в директории `static/css/`

## Контакты для поддержки

При возникновении вопросов или проблем обращайтесь по адресу: support@candlehouse.ru
