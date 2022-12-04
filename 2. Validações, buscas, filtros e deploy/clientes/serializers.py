from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Nome não deve conter números'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF está inválido'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve conter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O Celular é inválido -> modelo: 00 00000-0000'})
        return data
    