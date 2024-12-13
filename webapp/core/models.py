from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CoreModel(models.Model):

    soft_delete = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At")
    )
    deleted_at = models.DateTimeField(
        _("Deleted At"), editable=False,
        null=True, blank=True
    )

    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("created by user"),
        editable=False, null=True, blank=True,
        related_name="+", on_delete=models.SET_NULL
    )
    user_updated = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("updated by user"),
        editable=False, null=True, blank=True,
        related_name="+", on_delete=models.SET_NULL
    )
    user_deleted = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("deleted by user"),
        editable=False, null=True, blank=True,
        related_name="+", on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True

    @classmethod
    def get_all_fields(cls):
        """Return a list of all fields in the model."""
        return [field.name for field in cls._meta.get_fields()]

    @classmethod
    def get_simple_fields(cls):
        """Return a list of all non-relation fields."""
        return [field.name for field in cls._meta.get_fields() if not field.is_relation]

    @classmethod
    def get_related_fields(cls):
        """Return a list of all relation fields."""
        return [field.name for field in cls._meta.get_fields() if field.is_relation]

    def delete(self, soft=True, *args, **kwargs):
        """
        Soft-delete or hard-delete the object based on 'Soft' parameter.

        This method allows soft-deleting the object by marking it as removed
        and setting the 'time_deleted' attribute. If 'soft' parameter is False,
        the object is hard-deleted from the database.

        Args:
            soft (bool): A boolean indicating whether to soft-delete the
                object (default is True).

        Returns:
            None
        """

        if settings.DEBUG:
            soft = False

        if soft:
            # soft-delete instance
            self.soft_delete = True
            self.time_deleted = timezone.now()
            self.save()
        else:
            # delete from DB
            super().delete(*args, **kwargs)
