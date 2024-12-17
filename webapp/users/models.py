from django.utils.translation import gettext_lazy as _
from django.db import models
# from core.models import CoreModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from library.models import Book, Loan
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


def set_library_uesr_permission(user):
    user_permissions: list = [
        Permission.objects.get(
            codename='view_book',
            content_type=ContentType.objects.get_for_model(Book)
        ),
        Permission.objects.get(
            codename='add_loan',
            content_type=ContentType.objects.get_for_model(Loan)
        ),
        Permission.objects.get(
            codename='change_loan',
            content_type=ContentType.objects.get_for_model(Loan)
        ),
    ]

    user.user_permissions.add(*user_permissions)
