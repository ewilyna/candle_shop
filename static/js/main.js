/* 
 * Клиентская валидация форм для интернет-магазина ароматических свечей
 */

document.addEventListener('DOMContentLoaded', function() {
    // Валидация формы регистрации
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            if (!validateRegisterForm()) {
                event.preventDefault();
            }
        });
    }

    // Валидация формы входа
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            if (!validateLoginForm()) {
                event.preventDefault();
            }
        });
    }

    // Валидация формы оформления заказа
    const checkoutForm = document.getElementById('checkout-form');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function(event) {
            if (!validateCheckoutForm()) {
                event.preventDefault();
            }
        });
    }

    // Валидация формы обновления профиля
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.addEventListener('submit', function(event) {
            if (!validateProfileForm()) {
                event.preventDefault();
            }
        });
    }

    // Обновление количества товаров в корзине
    const quantityInputs = document.querySelectorAll('.cart-quantity-input');
    if (quantityInputs) {
        quantityInputs.forEach(input => {
            input.addEventListener('change', function() {
                validateQuantity(this);
            });
        });
    }
});

// Функция валидации формы регистрации
function validateRegisterForm() {
    let isValid = true;
    const username = document.getElementById('id_username');
    const email = document.getElementById('id_email');
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    const firstName = document.getElementById('id_first_name');
    const lastName = document.getElementById('id_last_name');
    
    // Проверка имени пользователя
    if (username && !username.value.trim()) {
        showError(username, 'Имя пользователя обязательно');
        isValid = false;
    } else if (username && username.value.length < 3) {
        showError(username, 'Имя пользователя должно содержать не менее 3 символов');
        isValid = false;
    } else if (username) {
        clearError(username);
    }
    
    // Проверка email
    if (email && !validateEmail(email.value)) {
        showError(email, 'Введите корректный email адрес');
        isValid = false;
    } else if (email) {
        clearError(email);
    }
    
    // Проверка имени и фамилии
    if (firstName && !firstName.value.trim()) {
        showError(firstName, 'Имя обязательно');
        isValid = false;
    } else if (firstName) {
        clearError(firstName);
    }
    
    if (lastName && !lastName.value.trim()) {
        showError(lastName, 'Фамилия обязательна');
        isValid = false;
    } else if (lastName) {
        clearError(lastName);
    }
    
    // Проверка паролей
    if (password1 && !password1.value) {
        showError(password1, 'Пароль обязателен');
        isValid = false;
    } else if (password1 && password1.value.length < 8) {
        showError(password1, 'Пароль должен содержать не менее 8 символов');
        isValid = false;
    } else if (password1) {
        clearError(password1);
    }
    
    if (password2 && password1 && password2.value !== password1.value) {
        showError(password2, 'Пароли не совпадают');
        isValid = false;
    } else if (password2) {
        clearError(password2);
    }
    
    return isValid;
}

// Функция валидации формы входа
function validateLoginForm() {
    let isValid = true;
    const username = document.getElementById('id_username');
    const password = document.getElementById('id_password');
    
    if (username && !username.value.trim()) {
        showError(username, 'Введите имя пользователя');
        isValid = false;
    } else if (username) {
        clearError(username);
    }
    
    if (password && !password.value) {
        showError(password, 'Введите пароль');
        isValid = false;
    } else if (password) {
        clearError(password);
    }
    
    return isValid;
}

// Функция валидации формы оформления заказа
function validateCheckoutForm() {
    let isValid = true;
    const firstName = document.getElementById('first_name');
    const lastName = document.getElementById('last_name');
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const address = document.getElementById('address');
    
    if (firstName && !firstName.value.trim()) {
        showError(firstName, 'Имя обязательно');
        isValid = false;
    } else if (firstName) {
        clearError(firstName);
    }
    
    if (lastName && !lastName.value.trim()) {
        showError(lastName, 'Фамилия обязательна');
        isValid = false;
    } else if (lastName) {
        clearError(lastName);
    }
    
    if (email && !validateEmail(email.value)) {
        showError(email, 'Введите корректный email адрес');
        isValid = false;
    } else if (email) {
        clearError(email);
    }
    
    if (phone && !validatePhone(phone.value)) {
        showError(phone, 'Введите корректный номер телефона');
        isValid = false;
    } else if (phone) {
        clearError(phone);
    }
    
    if (address && !address.value.trim()) {
        showError(address, 'Адрес доставки обязателен');
        isValid = false;
    } else if (address) {
        clearError(address);
    }
    
    return isValid;
}

// Функция валидации формы профиля
function validateProfileForm() {
    let isValid = true;
    const email = document.getElementById('id_email');
    const firstName = document.getElementById('id_first_name');
    const lastName = document.getElementById('id_last_name');
    const phone = document.getElementById('id_phone');
    
    if (email && !validateEmail(email.value)) {
        showError(email, 'Введите корректный email адрес');
        isValid = false;
    } else if (email) {
        clearError(email);
    }
    
    if (firstName && !firstName.value.trim()) {
        showError(firstName, 'Имя обязательно');
        isValid = false;
    } else if (firstName) {
        clearError(firstName);
    }
    
    if (lastName && !lastName.value.trim()) {
        showError(lastName, 'Фамилия обязательна');
        isValid = false;
    } else if (lastName) {
        clearError(lastName);
    }
    
    if (phone && phone.value && !validatePhone(phone.value)) {
        showError(phone, 'Введите корректный номер телефона');
        isValid = false;
    } else if (phone) {
        clearError(phone);
    }
    
    return isValid;
}

// Функция валидации количества товаров
function validateQuantity(input) {
    const min = parseInt(input.getAttribute('min'));
    const max = parseInt(input.getAttribute('max'));
    const value = parseInt(input.value);
    
    if (isNaN(value) || value < min) {
        input.value = min;
    } else if (value > max) {
        input.value = max;
    }
}

// Вспомогательные функции
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function validatePhone(phone) {
    const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    return re.test(String(phone));
}

function showError(input, message) {
    const formGroup = input.closest('.form-group') || input.parentElement;
    const errorElement = formGroup.querySelector('.invalid-feedback') || document.createElement('div');
    
    errorElement.className = 'invalid-feedback';
    errorElement.textContent = message;
    
    if (!formGroup.querySelector('.invalid-feedback')) {
        formGroup.appendChild(errorElement);
    }
    
    input.classList.add('is-invalid');
}

function clearError(input) {
    input.classList.remove('is-invalid');
    const formGroup = input.closest('.form-group') || input.parentElement;
    const errorElement = formGroup.querySelector('.invalid-feedback');
    
    if (errorElement) {
        errorElement.remove();
    }
}
