from django.db import models
from django.utils import timezone
class Abogado(models.Model):
    #Eleccion de especialidad
        ESPECIALIDAD_CHOICES=[
      ('Penal', 'Penal'),
      ('laboral', 'Laboral'),
      ('Civil','Civil'),
      ]
    # Atributos del abogado
        nombrea = models.CharField(max_length=144, blank=False, null=False)
        apellido = models.CharField(max_length=144, blank=False, null=False)
        celular = models.CharField(max_length=10, blank=False, null=False)
        correo = models.CharField(max_length=144, blank=False, null=False)
        tipos_especialidad = models.CharField(max_length=10, default='Penal', choices=ESPECIALIDAD_CHOICES)
        def __str__(self) -> str:
            return f'{self.nombrea}'
        
class Clientes(models.Model):
    # Atributos del cliente
        nombrec = models.CharField(max_length=144, blank=False, null=False)
        apellido = models.CharField(max_length=144, blank=False, null=False)
        direccion = models.CharField(max_length=144, blank=False, null=False)
        celular = models.CharField(max_length=10, blank=False, null=False)
        correo = models.CharField(max_length=144, blank=False, null=False)  

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
        
class Casos(models.Model):
        CASOS_CHOICES=[
      ('Penal', 'Penal'),
      ('laboral', 'Laboral'),
      ('Civil','Civil'),
      ]
        ESTADO_CHOICES=[
      ('Proceso', 'Proceso'),
      ('Cerrado', 'Cerrado'),
      ]
    # Atributos de los casos
        abogado = models.ForeignKey(Abogado, related_name='casos', on_delete=models.CASCADE)
        cliente = models.ForeignKey(Clientes, related_name='casos', on_delete=models.CASCADE)
        tipos_casos = models.CharField(max_length=10, default='Penal', choices=CASOS_CHOICES)
        Estado = models.CharField(max_length=10, default='Proceso', choices=ESTADO_CHOICES)
        fecha_apertura = models.DateTimeField(default=timezone.now)
        descripcion = models.TextField(blank=True, null=True)

        def __str__(self) -> str:
            return f'El abogado {self.abogado.nombrea} trata al cliente {self.cliente.nombrec}'
        
class Documentos(models.Model):
    # Atributos del documento
    caso = models.ForeignKey(Casos, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    descripcion_documento = models.TextField()
    archivo_adjunto = models.TextField(blank=False, null=False) # Puedes cambiar esto a FileField si necesitas almacenar archivos
    otros_campos = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f'Documento {self.tipo_documento} para el caso {self.caso.id}'
        
        