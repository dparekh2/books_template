from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("",
         views.BooksView.as_view(),
         name="books"),
    path("members/",
         views.MemberView.as_view(),
         name='members'),
    path("reserve/book/<int:book_id>/member/<int:member_id>/",
         views.ReserveView.as_view(),
         name='reserve')
]