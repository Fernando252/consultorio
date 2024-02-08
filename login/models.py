from django.db import models
from django.utils import timezone
class Abogado(models.Model):
    # Atributos del abogado
        nombrea = models.CharField(max_length=144, blank=False, null=False)
        apellido = models.CharField(max_length=144, blank=False, null=False)
        celular = models.CharField(max_length=10, blank=False, null=False)
        correo = models.CharField(max_length=10, blank=False, null=False)
        def __str__(self) -> str:
            return f'{self.nombrea}'
class Clientes(models.Model):
    # Atributos del cliente
        nombrec = models.CharField(max_length=144, blank=False, null=False)
        apellido = models.CharField(max_length=144, blank=False, null=False)
        direccion = models.CharField(max_length=144, blank=False, null=False)
        celular = models.CharField(max_length=10, blank=False, null=False)
        correo = models.CharField(max_length=10, blank=False, null=False)  

        def __str__(self) -> str:
            return f'{self.nombrec}'

class Cita(models.Model):
    # Atributos de la cita
        abogado = models.ForeignKey(Abogado, related_name='citas', on_delete=models.CASCADE)
        cliente = models.ForeignKey(Clientes, related_name='citas', on_delete=models.CASCADE)
        fecha_cita = models.DateTimeField()
        lugar_cita = models.CharField(max_length=255, blank=True, null=True)
        descripcion = models.TextField(blank=True, null=True)
        fecha_creacion = models.DateTimeField(default=timezone.now)   

        def __str__(self) -> str:
            return f'Cita con {self.abogado.nombrea} el {self.fecha_cita}'