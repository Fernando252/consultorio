# Generated by Django 4.2.7 on 2024-02-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_alter_abogado_contraseña_alter_clientes_contraseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$9xWU44DvZtaLN2GNz1EPgD$eWwgZBdLMUxNunKTy+cWhwENDYot7dx1CUbyODI79JM=', max_length=128),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$g6PD11yfvLPoWmLBVkYKET$3+drUKOFsJQZyUAOUDOkyil2Vui3uSJv5Mxo7g/wpdA=', max_length=128),
        ),
    ]
