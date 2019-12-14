from django.db import models

# Create your models here.

class Cliente(models.Model):
    pessoa_fisica = 'FIS'
    pessoa_juridica = 'JUR'
    cliente_tipo_opcoes = [
        (pessoa_fisica, 'Pessoa Física'),
        (pessoa_juridica, 'Pessoa Jurídica'),
    ]
    cliente_tipo = models.CharField(
        max_length = 3,
        choices = cliente_tipo_opcoes,
    )
    cliente_nome_fantasia = models.CharField(max_length=200)
    cliente_razao_social = models.CharField(max_length=200)
    cliente_nome_contato = models.CharField(max_length=200)
    cliente_cep = models.CharField(max_length=200)
    cliente_rua = models.CharField(max_length=200)
    cliente_numero = models.CharField(max_length=200)
    cliente_complemento = models.CharField(max_length=200)
    cliente_cidade = models.CharField(max_length=200)
    cliente_email = models.EmailField(max_length=254)
    cliente_telefone = models.CharField(max_length=200)
    segunda = 'SEG'
    terca = 'TER'
    quarta = 'QUA'
    quinta = 'QUI'
    sexta = 'SEX'
    sabado = 'SAB'
    domingo = 'DOM'
    cliente_entrega_opcoes = [
        (segunda, 'Segunda-Feira'),
        (terca, 'Terça-Feira'),
        (quarta, 'Quarta-Feira'),
        (quinta, 'Quinta-Feira'),
        (sexta, 'Sexta-Feira'),
        (sabado, 'Sábado'),
        (domingo, 'Domingo'),
    ]
    cliente_dias_entrega = models.CharField(
        max_length = 3,
        choices = cliente_entrega_opcoes,
    )
    cliente_lista_precos = models.PositiveIntegerField()
    cliente_ativo = models.BooleanField()