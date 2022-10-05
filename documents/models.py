from django.db import models

class transaction(models.TextChoices):
    DEBIT = "Débito"
    TICKET = "Boleto"
    FINANCING = "Financiamento"
    CREDIT = "Crédito"
    RECEIVING_LOAN = "Recebimento Empréstimo"
    SALES = "Vendas"
    RECEIPT_TED = "Recebimento TED"
    RECEIPT_DOC = "Recebimento DOC"
    RENT = "Aluguel"
    DEFAULT = "Nada"

class Document(models.Model):
    type = models.CharField(max_length=22)
    date = models.CharField(max_length=9)
    value = models.CharField(max_length=11)
    cpf = models.CharField(max_length=12)
    card = models.CharField(max_length=13)
    hour = models.CharField(max_length=7)
    store_owner = models.CharField(max_length=15)
    store_name = models.CharField(max_length=20)



