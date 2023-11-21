# Generated by Django 4.2.7 on 2023-11-20 21:53

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 18, 53, 18, 528254)),
        ),
        migrations.AddField(
            model_name='review',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]