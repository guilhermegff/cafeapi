from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from datetime import date

class Conta(models.Model):
    
    cd_cliente = models.ForeignKey(User)
    
    saldo = models.IntegerField(default=0)

    def __unicode__(self):
	
	return self.saldo

    def get_absolute_url(self):

    	return reverse('conta_detail', args=[str(self.id)])


class Cliente(models.Model):
    
    nome = models.CharField(max_length=40, default='0')
    cpf = models.CharField(max_length=20, default='0')

    def __unicode__(self):

    	return self.nome

class Maquina(models.Model):

    nome_maq = models.CharField(max_length=30, default='Maquina')
    estoque = models.IntegerField(default=0)

    def __unicode__(self):

        return self.nome_maq
