# Generated by Django 3.2.24 on 2024-02-10 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20240210_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abogado',
            name='user',
        ),
    ]
