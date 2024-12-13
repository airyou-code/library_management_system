from django.contrib import admin
from core.admin import CoreAdmin
from .models import Book, Loan


@admin.register(Book)
class BookAdmin(CoreAdmin):
    fieldsets = (
        ("Basic Information", {
            'fields': ('title', 'author', 'ISBN', 'page_count')
        }),
        ("Availability", {
            'fields': ('availability',)
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
