# Generated by Django 4.2.7 on 2024-02-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20240214_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$DwxrBzTM9P4MBIIxI8CK5K$a6cb8HP7Dol6lKARWnAVe2iNPe/e9NIgqRR0xFtSgG4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$0u4btvF57UNcDdLdF7nDyi$z4MVQdSzWqH/tVsppat5djXGYc+QGvHu593rZFod9z4=', max_length=128),
        ),
    ]
