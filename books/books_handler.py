from django.db.models import Avg, F, Count

from .models import (
    Book,
    Reservation
)


class BooksHandler:

    def is_book_available(self, book):
        is_available = False
        if book.available_copies:
            is_available = True
        return is_available

    def generate_book_response(self, book):
        return {
            'id': book.id,
            'name': book.name,
            'author': book.author.name,
            'is_available': self.is_book_available(book),
            'available_copies': book.available_copies
        }

    def get_all_available_books(self):
        books = Book.objects.order_by('-name')
        return [self.generate_book_response(
            book) for book in books]

    def get_books_analytics(self):
        return {
            'most_popular_books': Book.objects.all().order_by(
                'reservation').values_list('name')[0:5],
            'avg_checkout_duration': Reservation.objects.annotate(
                diff=F('due_date') - F('start_date')).aggregate(
                duration=Avg('diff')),
            'most_active_members': Reservation.objects.all().annotate(
                active=Count('member')).values_list('member__first_name')[0:3]
        }
