# Generated by Django 5.1.3 on 2024-11-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorrowedBooks', '0002_remove_borrowedbooks_booknumber_borrowedbooks_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbooks',
            name='bookNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
