from django.db import models


class Materias(models.Model):
    nombre = models.CharField('Nombre de Materia', max_length=50)
    codigo = models.CharField('Codigo de Materia', max_length=10)
    unidadesC = models.PositiveIntegerField('Unidades Curriculares')

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Materias"

    def __str__(self):
        return self.nombre


class Trimestre(models.Model):
    codigo = models.CharField(max_length=10)
    materias = models.ManyToManyField(Materias)
    Trayecto = models.PositiveIntegerField('Trayecto', null=True)

    def __str__(self):
        return self.codigo


class PNF(models.Model):
    nombre = models.CharField(max_length=20)
    trimetres = models.ManyToManyField(Trimestre)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "PNF"

    def __str__(self):
        return self.nombre


class Salones(models.Model):
    codigo = models.CharField(max_length=10)
    pnf = models.ManyToManyField(PNF, "pnf", null=True)

    def __str__(self):
        return self.codigo


class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    pnf = models.ForeignKey(PNF, null=True, on_delete=models.DO_NOTHING)
    materias = models.ManyToManyField(Materias, blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre


class Secciones(models.Model):
    modalidades = [('FS', "fin de semana"), ('ES', "entre semana")]

    codigo = models.CharField(max_length=10)
    pnf = models.ForeignKey(PNF, null=True, on_delete=models.CASCADE)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.DO_NOTHING)
    modalidad = models.CharField(max_length=30, choices=modalidades)
    profesores = models.ManyToManyField(Profesores)

    class Meta:
        ordering = ["codigo"]
        verbose_name_plural = "Secciones"

    def __str__(self):  # __unicode__ en Python 3
        return self.codigo


class Horarios(models.Model):
    codigo = models.CharField(max_length=10, default=None)
    seccion = models.ForeignKey(Secciones, null=True, on_delete=models.CASCADE)
    posicion = models.TextField(max_length=500, default=None)

    class Meta:
        ordering = ["codigo"]
        verbose_name_plural = "Secciones"

    def __str__(self):  # __unicode__ en Python 3
        return self.codigo

