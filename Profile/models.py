from django.db import models
from django.utils import timezone

# Create your models here.
class CiudadModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Ciudad'

class GeneroModel(models.Model):
    genero = models.CharField(max_length=50, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genero

    class Meta:
        db_table = 'Genero'

class OcupacionModel(models.Model):
    ocupacion = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion

    class Meta:
        db_table = 'Ocupacion'

class EstadoModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Estado'

class EstadoCivilModel(models.Model):
    estadoCivil = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estadoCivil

    class Meta:
        db_table = 'EstadoCivil'

class ProfileModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apPat = models.CharField(max_length=254, null=False)
    apMat = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(CiudadModel,on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroModel,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(OcupacionModel,on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoModel,on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(EstadoCivilModel,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Profile'