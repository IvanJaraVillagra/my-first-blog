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
	Trabajo = models.CharField(max_length=200)
	NumTajeta = models.CharField(max_length=20)
	TipoBanco = models.CharField(max_length=30)

	def __str__(self):
		return self.Run

class Mantencion(models.Model):
	CodManten=models.CharField(max_length=30)
	FechaMante=models.DateField()
	CodBici=models.CharField(max_length=30)
	Descripcion=models.CharField(max_length=300)

	def __str__(self):
		return self.CodManten

class Tarjeta(models.Model):
	TarjetaPrepa = models.CharField(max_length=30)

	def __str__(self):
		return self.TarjetaPrepa