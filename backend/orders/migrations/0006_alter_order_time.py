# Generated by Django 5.1 on 2024-09-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_order_date_alter_order_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="time",
            field=models.TimeField(default="17:36:27"),
        ),
    ]
