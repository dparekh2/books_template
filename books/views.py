from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    Author,
    Book,
    Member,
    Reservation,
    Checkout
)


class IndexView(generic.ListView):

    def get_books(self):
        """Return all books."""
        return Book.objects.all()

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"
#
#
# def vote(request, question_id):
#     ...  # same as above, no changes needed.