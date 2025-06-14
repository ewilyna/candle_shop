from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from .forms import UserRegisterForm, UserUpdateForm

def register(request):
    """
    Представление для регистрации нового пользователя
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, _('Ваш аккаунт создан! Теперь вы можете войти в систему.'))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': _('Регистрация')})

@login_required
def profile(request):
    """
    Представление для просмотра и редактирования профиля пользователя
    """
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Ваш профиль успешно обновлен!'))
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'title': _('Личный кабинет')
    }
    return render(request, 'users/profile.html', context)

@login_required
def order_history(request):
    """
    Представление для просмотра истории заказов пользователя
    """
    orders = request.user.orders.all().order_by('-created')
    return render(request, 'users/order_history.html', {
        'orders': orders,
        'title': _('История заказов')
    })
