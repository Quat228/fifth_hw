# Generated by Django 4.1.7 on 2023-03-21 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_remove_order_ingredient_order_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredients',
        ),
    ]
