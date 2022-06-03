from time import strftime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):

    titulo = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateField(auto_now=True)
    usuarios = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
       return self.data_evento.strftime('%d/%m/%Y %H:%M')
