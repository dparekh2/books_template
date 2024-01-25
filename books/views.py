from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .books_handler import BooksHandler
from .member_handler import MemberHandler


class BooksView(APIView):

    def get(self, request, *args, **kwargs):
        data = BooksHandler().get_all_available_books()
        return Response(data=data, status=status.HTTP_200_OK)


class MemberView(APIView):

    def get(self, request, *args, **kwargs):
        data = MemberHandler().get_member_data()
        return Response(data=data, status=status.HTTP_200_OK)


class ReserveView(APIView):

    def post(self, request, *args, **kwargs):
        member_id = kwargs.get('member_id')
        book_id = kwargs.get('book_id')
        start_date = request.data.get('start_date')
        due_date = request.data.get('due_date')
        data = MemberHandler().reserve_book(
            member_id, book_id, start_date, due_date)
        return Response(data=data, status=status.HTTP_200_OK)
