# Generated by Django 4.2.7 on 2024-02-16 03:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_alter_abogado_contraseña_alter_clientes_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$5tF30DODCRj2Xe0njeSkdn$dpfHElPshY2zZNHJcc88G2bzIZHsZE9HF1MMRRr2t94=', max_length=128),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$600000$r6Ixa8VOy0GDpBnPBABjly$ul4pbxvyWQoH/X3efymPI5phayivvyluw8TU31IXyT8=', max_length=128),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='archivo_adjunto',
            field=models.FileField(blank=True, upload_to='documentos/'),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
