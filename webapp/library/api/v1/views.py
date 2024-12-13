from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from library.models import Book, Loan
from .serializers import BookSerializer, LoanSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['author', 'availability']
    ordering_fields = ['title', 'author']
    search_fields = ['title', 'author']


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.availability:
            raise ValidationError("This book is not available.")
        book.availability = False
        book.save()
        serializer.save(user=self.request.user, status='borrowed')

    def perform_update(self, serializer):
        instance = self.get_object()
        if serializer.validated_data.get('status') == 'returned':
            instance.book.availability = True
            instance.book.save()
        serializer.save()
