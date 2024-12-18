from django.utils.translation import gettext_lazy as _
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


@admin.register(Loan)
class LoanAdmin(CoreAdmin):
    fieldsets = (
        ("Loan Book", {
            'fields': (
                'user', 'book',
                'borrow_date',
                'return_date',
                'status'
            )
        }),
    )
    readonly_fields = ('borrow_date',)
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    search_fields = ('book__title', 'user__username')
    list_filter = ('status', 'borrow_date', 'return_date')

    def get_readonly_fields(self, request, obj=None) -> list:
        if not (
            request.user.is_admin or request.user.is_superuser
        ) and request.user.is_registered_user:
            readonly_fields = (
                'user',
                *self.readonly_fields,
            )
            if obj and obj.created_at:
                readonly_fields = [
                    'book',
                    *readonly_fields
                ]
            return readonly_fields
        return super().get_readonly_fields(request, obj=None)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not (
            request.user.is_admin or request.user.is_superuser
        ) and request.user.is_registered_user:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        if not (
            request.user.is_admin or request.user.is_superuser
        ) and request.user.is_registered_user:
            obj.user = request.user

        if not obj.book.availability:
            self.message_user(
                request,
                _("This book is not available."),
                level='ERROR'
            )
        else:
            if not change:
                obj.book.availability = False
                obj.book.save()
            else:
                super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'book':
            kwargs["queryset"] = Book.objects.filter(availability=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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
    list_display = ('get_fullname', 'birth_date', 'nationality')
    search_fields = (
        'first_name',
        'last_name'
    )
    list_filter = (
        'first_name',
        'last_name',
        'nationality',
    )

    def get_fullname(self, obj: Author):
        return obj.__str__()
    get_fullname.short_description = _("Full Name")
    get_fullname.admin_order_field = 'first_name'
