from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("", views.IndexView.as_view(),
         name="index"),
    # path("book/<str:book>/author/<str:author_id>/",
    #      views.BooksView.as_view(), name="books"),
    # path("<int:pk>/results/", views.ResultsView.as_view(),
    #      name="results"),
    # path("<int:question_id>/vote/", views.vote,
    #      name="vote"),
]