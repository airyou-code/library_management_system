from django.utils.translation import gettext_lazy as _
from django.db import models
# from core.models import CoreModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# Create your models here.


class LibraryUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('user', 'Registered User'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name=_("Role")
    )

    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_registered_user(self):
        return self.role == 'user'
