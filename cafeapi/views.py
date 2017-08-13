from django.contrib.auth.models import User
from .models import Conta, Cliente, Maquina
from django.shortcuts import render
from serializers import ContaSerializer, ClienteSerializer, MaquinaSerializer, UserSerializer
from rest_framework import generics


class ContaList(generics.ListCreateAPIView):
    lookup_url_kwarg = 'cliente'
    serializer_class = ContaSerializer

    def get_queryset(self):
	cd_cliente = self.kwargs.get(self.lookup_url_kwarg)
	contas = Conta.objects.filter(cd_cliente = cd_cliente)
	return contas

class ContaDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = ('id')
    serializer_class = ContaSerializer

    def get_queryset(self):
	id = self.kwargs.get(self.lookup_url_kwarg)
	conta = Conta.objects.filter(id=id)
	return conta

class ClienteList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = ('id_cli')
    serializer_class = ClienteSerializer

    def get_queryset(self):
	id_cli = self.kwargs.get(self.lookup_url_kwarg)
	cliente = Cliente.objects.filter(id=id_cli)
	return cliente

class MaquinaList(generics.ListCreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    

class MaquinaDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = ('maq')
    serializer_class = MaquinaSerializer

    def get_queryset(self):
	maq = self.kwargs.get(self.lookup_url_kwarg)
	maquina = Maquina.objects.filter(id=maq)
	return maquina



