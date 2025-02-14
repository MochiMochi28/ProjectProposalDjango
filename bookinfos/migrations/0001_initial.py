# Generated by Django 5.1.3 on 2024-11-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('datePublished', models.DateField()),
                ('bookNumber', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('sections', models.CharField(default='Others', max_length=20)),
            ],
        ),
    ]
