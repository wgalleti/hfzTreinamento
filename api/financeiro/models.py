from django.db import models


class Fornecedor(models.Model):
    """
    Cadastro de Fornecedores
    """
    nome = models.CharField(
        max_length=50
    )
    cpf_cnpj = models.CharField(
        max_length=20,
        unique=True
    )
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'


class Conta(models.Model):
    """
    Conta financeira, onde será controlado saldo de dinheiro
    Vai ter movimentos, Entradas e Saidas
    """
    descricao = models.CharField(
        max_length=50
    )
    saldo_inicial = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.descricao


class Titulo(models.Model):
    """
    Cadastro de titulos para pagamento (Boletos, Faturas e etc)
    """
    data = models.DateField()
    fornecedor = models.ForeignKey(
        to='financeiro.Fornecedor',
        on_delete=models.DO_NOTHING
    )
    numero_documento = models.CharField(
        max_length=50
    )
    vencimento = models.DateField()
    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.numero_documento


class Pagamento(models.Model):
    """
    Efetivação dos pagamentos
    """
    data = models.DateField()
    titulo = models.ForeignKey(
        to='financeiro.Titulo',
        on_delete=models.DO_NOTHING
    )
    conta = models.ForeignKey(
        to='financeiro.Conta',
        on_delete=models.DO_NOTHING
    )
    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f'{self.pk}'
