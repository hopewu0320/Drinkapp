# Generated by Django 4.1.5 on 2023-02-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_alter_cart_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="amount",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
