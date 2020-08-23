from django.db import models

# Create your models here.
class TarefaBd(models.Model):
    conteudo=models.CharField(max_length=1000)
    data=models.DateTimeField(auto_now_add=True)
    completado=models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)