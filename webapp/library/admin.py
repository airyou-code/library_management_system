from django.contrib import admin
from core.admin import CoreAdmin
from .models import Book, Loan, Author


@admin.register(Book)
class BookAdmin(CoreAdmin):
    fieldsets = (
        ("Basic Information", {
            'fields': (
                'title',
                'author',
                'description',
                'ISBN',
                'page_count',
                'availability'
            )
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'ISBN', 'availability', 'created_at')
    search_fields = ('title', 'author', 'ISBN')
    list_filter = (
        'created_at',
        'updated_at',
        'availability',
    )

    # def has_view_permission(self, request, obj=None):
    #     """Allow all users with role 'user' or higher to view the model."""
    #     return True
    #     return request.user.is_authenticated and (
    #         request.user.role == 'user' or request.user.is_admin
    #     )

    # def has_add_permission(self, request):
    #     """Allow users with role 'user' to add books."""
    #     return True
    #     return request.user.is_authenticated and request.user.role == 'user'

    # def has_change_permission(self, request, obj=None):
    #     return True
    #     """Allow editing only if the user is an admin."""
    #     return request.user.is_admin

    # def has_delete_permission(self, request, obj=None):
    #     return True
    #     """Allow deletion only for admins."""
    #     return request.user.is_admin


@admin.register(Loan)
class LoanAdmin(CoreAdmin):
    fieldsets = (
        ("User and Book", {
            'fields': ('user', 'book')
        }),
        ("Dates and Status", {
            'fields': ('borrow_date', 'return_date', 'status')
        }),
    )
    readonly_fields = ('borrow_date',)
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    search_fields = ('book__title', 'user__username')
    list_filter = ('status', 'borrow_date', 'return_date')


@admin.register(Author)
class AuthorAdmin(CoreAdmin):
    fieldsets = (
        ("Author Info", {
            'fields': (
                'first_name',
                'last_name',
                'birth_date',
                'nationality',
                'biography',
            )
        }),
    )
    # readonly_fields = ()
    list_display = ('first_name', 'last_name', 'birth_date', 'nationality')
    search_fields = (
        'first_name',
        'last_name'
    )
    list_filter = (
        'first_name',
        'last_name',
        'nationality',
    )
