# Generated by Django 4.0.5 on 2022-06-09 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='count',
        ),
    ]
