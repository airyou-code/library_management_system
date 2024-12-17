from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import LibraryUser


@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model._meta.app_label = 'auth'
