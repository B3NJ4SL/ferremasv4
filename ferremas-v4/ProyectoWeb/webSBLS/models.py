from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='categoria_fotos/')

    def __str__(self) -> str:
        return super().__str__()    

class Trabajo(models.Model):
    idTrabajo=models.AutoField(primary_key=True)
    nombreTrabajo=models.CharField(max_length=80)          
    Usuarioreg=models.CharField(max_length=50)
    marcav=models.CharField(max_length=50,default="marca")
    modelov=models.CharField(max_length=50, default="modelo")
    annov=models.IntegerField(default=2010)
    preciv=models.IntegerField(default=100000)
    descripcion=models.TextField()
    foto=models.ImageField(upload_to='fotos',null=True,default='fotos/auto_default.jpg')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    publicado=models.BooleanField(default=True)
    comentario=models.TextField(null=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self) -> str:
        return self.nombreTrabajo


class Galeriaimg(models.Model):
    idFoto = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='galeria',null=True)
    trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.idFoto)+" "+(self,trabajo.nombreTrabajo)
    
class Contacto(models.Model):
    nombrep = models.CharField(max_length=100)
    correop = models.EmailField()
    mensajep = models.TextField()
    def __str__(self):
        return self.nombrep