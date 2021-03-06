from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

'''
class MiUser(AbstractUser):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "MiUser"
        verbose_name_plural = "MiUsers"

'''


class Curso(models.Model):

    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
