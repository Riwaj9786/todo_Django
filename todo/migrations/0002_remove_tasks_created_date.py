# Generated by Django 4.2 on 2023-05-17 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='created_date',
        ),
    ]
