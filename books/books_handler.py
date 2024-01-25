from .models import (
    Book
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
