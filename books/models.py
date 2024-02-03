from datetime import date, timedelta

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Member(models.Model):
    prefix = models.CharField(max_length=3, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        full_name = str(self.first_name) + ' ' + str(self.last_name)
        if self.prefix:
            return str(self.prefix) + ' ' + full_name
        else:
            return full_name


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    due_date = models.DateField(
        default=date.today() + timedelta(days=7))

    def __str__(self):
        if self.book and self.member:
            return str(self.book) + ' reserved by ' + str(self.member)


class Checkout(models.Model):
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE)
    overdue = models.BooleanField(default=False)
    fine_amount = models.IntegerField(default=0)
    is_returned = models.BooleanField(default=False)
