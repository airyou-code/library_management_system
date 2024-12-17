from rest_framework import serializers
from library.models import Book, Loan


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "book",
            "status",
        ]
        read_only_fields = ('borrow_date', 'status')
