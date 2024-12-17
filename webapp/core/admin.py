from django.utils.translation import gettext_lazy as _
from core.models import CoreModel
from django.contrib import admin

# Register your models here.
# admin.site.site_header = "Library Management System"
admin.site.site_header = "LMS"


class CoreAdmin(admin.ModelAdmin):
    """
    Admin class for managing the CoreModel.

    This class provides customization for the Django admin interface to
    manage the CoreModel. It defines actions, ordering, and sets
    fields as readonly or changeable based on certain conditions.
    """
    custom_fields: list = []
    change_fields: list = []
    # ordering = ("state")
    base_fields = CoreModel.get_all_fields()
    base_readonly = base_fields

    def get_fieldsets(self, request, obj=None):
        """Dynamically add the 'Meta Data' fieldset for superusers."""
        fieldsets = super().get_fieldsets(request, obj)

        # Only show "Meta Data" to superusers or admin
        if request.user.is_superuser or request.user.is_admin:
            fieldsets += (
                ("Meta Data", {
                    'fields': self.base_fields,
                }),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        """
        Save the CoreModel instance after modification.

        This method is called when a CoreModel instance is saved
        in the admin interface. It automatically sets the "user_created"
        and "user_updated" fields based on the request user.

        Args:
            request (HttpRequest):
                The HTTP request object.
            obj (CoreModel):
                The CoreModel instance being saved.
            form (ModelForm):
                The form used to modify the instance.
            change (bool):
                A boolean indicating if this is an existing
                instance being changed or a new one being created.

        Returns:
            None
        """
        if not obj.user_created:
            obj.user_created = request.user
            obj.user_updated = request.user
        else:
            obj.user_updated = request.user
        super(CoreAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None) -> list:
        """
        Retrieve the readonly fields based on the state of
        the CoreModel instance.

        This method is called to determine the readonly fields for
        the admin interface based on the state of the CoreModel instance.

        Args:
            request (HttpRequest):
                The HTTP request object.
            obj (CoreModel, optional):
                The CoreModel instance.
                Defaults to None.

        Returns:
            list: A list of readonly fields.
        """

        if obj and self.change_fields and obj.created_at:

            return [
                field.name for field in (
                    *self.model._meta.get_fields(),
                ) if field.name not in self.change_fields
            ] + [
                *self.base_readonly,
                *self.custom_fields
            ]

        return [
            *self.readonly_fields,
            *self.base_readonly,
            *self.custom_fields
        ]
