# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate

# Создание директории для фикстур, если она не существует
mkdir -p fixtures

# Запуск скрипта для создания демонстрационных товаров
echo "Запуск скрипта для создания демонстрационных товаров..."
python scripts/create_demo_products.py

echo "Демонстрационные товары успешно добавлены в базу данных!"
echo "Теперь вы можете запустить сервер и просмотреть товары в каталоге."
echo "Для запуска сервера выполните команду: python manage.py runserver"
