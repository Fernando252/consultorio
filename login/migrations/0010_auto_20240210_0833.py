# Generated by Django 3.2.24 on 2024-02-10 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0009_auto_20240208_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado',
            name='cedula',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='abogado',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cedula',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='abogado',
            name='tipos_especialidad',
            field=models.CharField(choices=[('Penal', 'Penal'), ('Laboral', 'Laboral'), ('Civil', 'Civil')], default='Penal', max_length=10),
        ),
    ]
