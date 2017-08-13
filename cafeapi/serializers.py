from django.contrib.auth.models import User
from rest_framework import serializers
from cafeapi.models import Conta, Cliente, Maquina

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
	model = Conta
	fields = ('id', 'cd_cliente', 'saldo')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
	model = Cliente
	fields = ('id', 'nome', 'cpf')

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
	model = Maquina
	fields = ('id', 'nome_maq', 'estoque')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
	model = User
	fields = ('id', 'username')
