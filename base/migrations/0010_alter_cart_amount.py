# Generated by Django 4.1.5 on 2023-02-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_remove_cart_total_cart_amount_cart_subtotal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="amount",
            field=models.IntegerField(null=True),
        ),
    ]