from .models import (
    Member,
    Reservation,
    Book
)

from .books_handler import BooksHandler
from .constants import ErrorMessages


class MemberHandler:

    def generate_reservation_response(self, reservation):
        return {
            'book': BooksHandler().generate_book_response(
                reservation.book),
            'start_date': reservation.start_date,
            'due_date': reservation.due_date
        }

    def generate_member_response(self, member):
        return {
            'id': member.id,
            'full_name': str(member),
            'reservations': self.get_member_reservations(
                member),
            'fines_due': None
        }

    def get_member_reservations(self, member):
        reservations = Reservation.objects.filter(member=member)
        return [self.generate_reservation_response(
            reservation) for reservation in reservations]

    def get_member_data(self):
        members = Member.objects.all()
        return [self.generate_member_response(
            member) for member in members]

    def reserve_book(
            self, member_id, book_id, start_date, due_date):
        book = Book.objects.get(id=book_id)
        if not BooksHandler().is_book_available(book):
            return {
                'error': ErrorMessages.NOT_IN_STOCK
            }

        member = Member.objects.get(id=member_id)

        Reservation.objects.create(
            book=book,
            member=member,
            start_date=start_date,
            due_date=due_date
        )

        book.available_copies = book.available_copies-1
        book.save()

        return self.generate_member_response(member)
