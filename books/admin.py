from django.contrib import admin

from django.contrib import admin

from .models import (
    Author,
    Book,
    Member,
    Reservation,
    Checkout
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "author",
        "available_copies"
    ]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "prefix",
        "first_name",
        "last_name"
    ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "book",
        "member",
        "start_date",
        "due_date"
    ]


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = [
        "reservation",
        "fine_amount",
        "is_returned"
    ]
