from rest_framework import viewsets
from .models import Fornecedor, Conta, Titulo, Pagamento
from .serializers import FornecedorSerializer, ContaSerializer, TituloSerializer, PagamentoSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all().order_by('pk')
    serializer_class = FornecedorSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all().order_by('pk')
    serializer_class = ContaSerializer


class TituloViewSet(viewsets.ModelViewSet):
    queryset = Titulo.objects.all().order_by('pk')
    serializer_class = TituloSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all().order_by('pk')
    serializer_class = PagamentoSerializer
