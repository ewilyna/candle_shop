from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import User

class UserRegisterForm(forms.ModelForm):
    """
    Форма регистрации пользователя с валидацией полей
    """
    password1 = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Введите пароль')}),
        min_length=8,
        help_text=_('Пароль должен содержать не менее 8 символов')
    )
    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Подтвердите пароль')}),
        help_text=_('Введите тот же пароль для подтверждения')
    )
    
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Введите email')}),
        error_messages={'invalid': _('Введите корректный email адрес')}
    )
    
    first_name = forms.CharField(
        label=_('Имя'),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите имя')}),
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁa-zA-Z\s-]+$',
                message=_('Имя может содержать только буквы, пробелы и дефисы')
            )
        ]
    )
    
    last_name = forms.CharField(
        label=_('Фамилия'),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите фамилию')}),
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁa-zA-Z\s-]+$',
                message=_('Фамилия может содержать только буквы, пробелы и дефисы')
            )
        ]
    )
    
    phone = forms.CharField(
        label=_('Телефон'),
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите номер телефона')}),
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{10,15}$',
                message=_('Введите корректный номер телефона (10-15 цифр)')
            )
        ]
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите имя пользователя')}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Введите адрес доставки'), 'rows': 3}),
        }
        help_texts = {
            'username': _('Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'),
        }
        error_messages = {
            'username': {
                'unique': _('Пользователь с таким именем уже существует.'),
            },
        }
    
    def clean_password2(self):
        """
        Проверка совпадения паролей
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return password2
    
    def clean_email(self):
        """
        Проверка уникальности email
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Пользователь с таким email уже существует'))
        return email
    
    def save(self, commit=True):
        """
        Сохранение пользователя с хешированием пароля
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления данных пользователя с валидацией полей
    """
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': _('Введите корректный email адрес')}
    )
    
    first_name = forms.CharField(
        label=_('Имя'),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁa-zA-Z\s-]+$',
                message=_('Имя может содержать только буквы, пробелы и дефисы')
            )
        ]
    )
    
    last_name = forms.CharField(
        label=_('Фамилия'),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁa-zA-Z\s-]+$',
                message=_('Фамилия может содержать только буквы, пробелы и дефисы')
            )
        ]
    )
    
    phone = forms.CharField(
        label=_('Телефон'),
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{10,15}$',
                message=_('Введите корректный номер телефона (10-15 цифр)')
            )
        ]
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
    def clean_email(self):
        """
        Проверка уникальности email
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(_('Пользователь с таким email уже существует'))
        return email
