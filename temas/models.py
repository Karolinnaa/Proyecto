from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tema(models.Model):
  titulo = models.CharField(max_length=200)
  descripcion = models.TextField(max_length=1000)
  creado = models.DateTimeField(auto_now_add=True)
  fecha = models.DateTimeField(null=True, blank=True)
  importante = models.BooleanField(default=False)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo + ' - ' + self.usuario.username
