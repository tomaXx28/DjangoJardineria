from django.db import models
# Create your models here.

class Usuario(models.Model):     # rut - Nombre - AppPaterno - appMaterno - fecha Nacimiento     # tipo - correo - telefono - activo     rut = models.CharField(max_length=10, primary_key=True)     nombre = models.CharField(max_length=50, blank=False, null=False)     appPaterno = models.CharField(max_length=30, blank=False, null=False)     appMaterno = models.CharField(max_length=30, blank=False, null=False)     correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)     cotraseña= models.CharField(max_length=50, blank=False, null=False)     activo = models.IntegerField()      def str(self):         return str(self.nombre)+" "+str(self.appPaterno)+" "+str(self.appMaterno)
    rut = models.CharField(max_length=10, primary_key=True)     
    nombre = models.CharField(max_length=50, blank=False, null=False)       
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)     
    cotraseña= models.CharField(max_length=50, blank=False, null=False)     
    activo = models.IntegerField()      
    def str(self):         
        return str(self.nombre)+" "+str(self.appPaterno)+" "+str(self.appMaterno)