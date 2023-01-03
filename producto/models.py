from django.db import models

# Create your models here.

class producto(models.Model):
    nombre=models.CharField(max_length=60)
    precio=models.FloatField()
    stock=models.IntegerField()
    imagen=models.ImageField(upload_to='productos')
    descripcion=models.CharField(max_length=400)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

        def __str__(self):
            return self.titulo

