# Generated by Django 3.2.24 on 2024-02-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20240208_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado',
            name='tipos_especialidad',
            field=models.CharField(choices=[('Penal', 'Penal'), ('laboral', 'Laboral'), ('Civil', 'Civil')], default='Penal', max_length=10),
        ),
    ]
