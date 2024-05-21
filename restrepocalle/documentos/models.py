from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombreC=models.CharField(max_length=30, verbose_name='Cliente')

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        

    def __str__(self):
        return self.nombreC
    
class Documento(models.Model):
    nombreD=models.CharField(max_length=30, verbose_name='Documento')

    class Meta:
        verbose_name='Documento'
        verbose_name_plural='Documentos'
        

    def __str__(self):
        return self.nombreD

"""class Codigo(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre"""

class Archivo(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    tipo=models.ForeignKey(Documento, on_delete=models.PROTECT )
    cliente=models.ForeignKey(Cliente, on_delete=models.PROTECT)
    #codigo=models.CharField(max_length=30)
    image = models.FileField(upload_to='Archivos/', verbose_name='Archivo')
    observaciones=models.TextField(max_length=250, blank=True)

    def __str__(self):
         txt="{0}"
         return txt.format(self.fecha)
    
    class Meta:
        verbose_name='Archivo'
        verbose_name_plural='Archivos'
        ordering =['fecha']  


