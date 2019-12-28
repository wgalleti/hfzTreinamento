from rest_framework import serializers
from .models import Fornecedor, Conta, Titulo, Pagamento


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'


class TituloSerializer(serializers.ModelSerializer):
    fornecedor_display = serializers.SerializerMethodField('_fornecedor')

    def _fornecedor(self, obj: Titulo):
        return FornecedorSerializer(obj.fornecedor).data

    class Meta:
        model = Titulo
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
