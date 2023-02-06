# Generated by Django 4.1.5 on 2023-02-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="total",
        ),
        migrations.AddField(
            model_name="cart",
            name="amount",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="cart",
            name="subtotal",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="drink",
            name="price",
            field=models.IntegerField(null=True),
        ),
    ]