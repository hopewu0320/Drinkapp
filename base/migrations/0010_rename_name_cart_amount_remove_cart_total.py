# Generated by Django 4.1.5 on 2023-02-06 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_cart_name_alter_cart_total_alter_drink_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="name",
            new_name="amount",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="total",
        ),
    ]
