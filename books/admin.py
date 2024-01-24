from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import (
    Author,
    Book,
    Member,
    Reservation,
    Checkout
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Reservation)
admin.site.register(Checkout)
