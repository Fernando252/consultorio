# Generated by Django 4.2.7 on 2024-02-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_alter_abogado_contraseña_alter_clientes_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$8m3ippgEs9TdsN3bJ1RnG8$67w6fWNIi85iw6ZhXHlEqyZm7otMt5H5cSw+ZwcqMJ4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$zjHRf63OII5De2u1SqRFHY$PhIXZfjHuvN8zxIC1pT1rl1+8kvG+p6kCJyIfo3Y/vg=', max_length=128),
        ),
    ]
