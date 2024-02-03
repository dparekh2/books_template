# Generated by Django 4.2.9 on 2024-02-03 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_member_prefix"),
    ]

    operations = [
        migrations.RenameField(
            model_name="checkout",
            old_name="reservation",
            new_name="reservation_checkouts",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="member",
            new_name="member_reservations",
        ),
        migrations.AddField(
            model_name="checkout",
            name="fine_amount",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="checkout",
            name="is_returned",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="due_date",
            field=models.DateField(default=datetime.date(2024, 2, 10)),
        ),
    ]
