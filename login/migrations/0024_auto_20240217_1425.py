# Generated by Django 3.2.24 on 2024-02-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_abogado_contraseña_alter_clientes_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$260000$MweXs5JzXkNuUO7WET8xjW$OvmZ1MQqZADDY06qa5bSzOzwM8By4gecWkDVnFJo9pM=', max_length=128),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contraseña',
            field=models.CharField(default='pbkdf2_sha256$260000$KkQ8jomvoUF6OFobjHukeN$2XyG4SukteVOmHp9akxwPWWYzwOqw4McmlFJQTpGJmo=', max_length=128),
        ),
    ]