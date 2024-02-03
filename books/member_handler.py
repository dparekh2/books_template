from datetime import date

from .models import (
    Book,
    Checkout,
    Member,
    Reservation
)

from .books_handler import BooksHandler
from .constants import ErrorMessages


class MemberHandler:

    def generate_reservation_response(self, reservation):
        checkouts = Checkout.objects.filter(
                reservation=reservation)
        return {
            'book': BooksHandler().generate_book_response(
                reservation.book),
            'is_checked_out': checkouts.exists(),
            'start_date': reservation.start_date,
            'due_date': reservation.due_date,
            'is_overdue': checkouts.first().is_overdue if checkouts else False
        }

    def refresh_fines(self, member_checkouts):
        for checkout in member_checkouts:
            if checkout.reservation.due_date < date.today:
                checkout.overdue = True
                days_late = (date.today() - checkout.reservation.due_date).days
                checkout.fine_amount = days_late * 50
                checkout.save()

    def get_member_fines(self, member):
        member_checkouts = Checkout.objects.filter(
            reservation__member=member)
        self.refresh_fines(member_checkouts)
        total_fines_due = 0
        for checkout in member_checkouts:
            if not checkout.is_returned:
                total_fines_due += checkout.fine_amount
        return total_fines_due

    def generate_member_response(self, member):
        return {
            'id': member.id,
            'full_name': str(member),
            'reservations': self.get_member_reservations(
                member),
            'fines_due': self.get_member_fines(member)
        }

    def get_member_reservations(self, member):
        reservations = Reservation.objects.filter(member=member)
        return [self.generate_reservation_response(
            reservation) for reservation in reservations]

    def get_member_data(self):
        members = Member.objects.all()
        return [self.generate_member_response(
            member) for member in members]

    def get_earliest_available_date(self, book):
        reservations = Reservation.objects.filter(book=book)
        if reservations:
            return reservations.earliest('due_date').due_date
        else:
            return {
                'error': ErrorMessages.NOT_IN_STOCK
            }

    def reserve_book(
            self, member_id, book_id, due_date):
        book = Book.objects.get(id=book_id)
        member = Member.objects.get(id=member_id)
        reservation = Reservation.objects.create(
            book=book, member=member)

        if BooksHandler().is_book_available(book):
            start_date = date.today
            Checkout.objects.create(
                reservation=reservation)
            book.available_copies = book.available_copies - 1
            book.save()
        else:
            start_date = self.get_earliest_available_date(book)

        reservation.start_date = start_date
        reservation.save()
        return self.generate_member_response(member)
