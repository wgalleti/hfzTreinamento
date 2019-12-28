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
    saldo = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        read_only=True
    )
    pago = serializers.BooleanField(
        read_only=True
    )

    titulo_display = serializers.CharField(
        max_length=255,
        read_only=True
    )

    def _fornecedor(self, obj: Titulo):
        return FornecedorSerializer(obj.fornecedor).data

    class Meta:
        model = Titulo
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
