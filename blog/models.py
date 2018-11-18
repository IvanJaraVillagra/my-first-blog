from django.db import models

class Post(models.Model):
	PrimerNombre = models.CharField(max_length=30)
	SegundoNombre = models.CharField(max_length=30)
	PrimerApellido = models.CharField(max_length=30)
	SegundoApellido = models.CharField(max_length=30)
	Run = models.CharField(max_length=10)
	dv = models.CharField(max_length=1)
	Telefono = models.IntegerField()
	Direccion = models.CharField(max_length=100)
	Comuna = models.CharField(max_length=50)
	Usuario = models.CharField(max_length=50)
	Contraseña = models.CharField(max_length=50)
	Correo = models.CharField(max_length=200)

	def __str__(self):
		return self.Run