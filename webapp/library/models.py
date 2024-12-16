from django.db import models
from core.models import CoreModel
from django_countries.fields import CountryField
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Author(CoreModel):
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("Birth Date")
    )
    nationality = CountryField(
        null=True, blank=True, verbose_name=_("Nationality")
    )
    biography = models.TextField(
        null=True, blank=True, verbose_name=_("Biography")
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(CoreModel):
    title = models.CharField(
        max_length=255, verbose_name=_("Title")
    )
    author = models.ForeignKey(
        "Author",
        on_delete=models.SET_NULL, null=True, verbose_name=_("Author")
    )
    ISBN = models.CharField(
        max_length=13, unique=True, verbose_name=_("ISBN")
    )
    description = models.TextField(null=True, blank=True)
    page_count = models.PositiveIntegerField(
        verbose_name=_("Page Count")
    )
    availability = models.BooleanField(
        default=True, verbose_name=_("Availability")
    )

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Loan(CoreModel):
    STATUS_CHOICES = (
        ("borrowed", _("Borrowed")),
        ("returned", _("Returned")),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, verbose_name=_("Book")
    )
    borrow_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Borrow Date")
    )
    return_date = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Return Date")
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="borrowed",
        verbose_name=_("Status"),
    )

    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"

    class Meta:
        verbose_name = _("Loan")
        verbose_name_plural = _("Loans")
