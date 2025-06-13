from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Расширенная модель пользователя с дополнительными полями
    """
    phone = models.CharField(_('Номер телефона'), max_length=15, blank=True, null=True)
    address = models.TextField(_('Адрес доставки'), blank=True, null=True)
    
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        
    def __str__(self):
        return self.username
