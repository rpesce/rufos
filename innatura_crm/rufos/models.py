from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

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
    cliente_nome_fantasia = models.CharField(max_length=200, help_text="Nome da empresa")
    cliente_razao_social = models.CharField(max_length=200, help_text="Razão social da empresa")
    cliente_nome_contato = models.CharField(max_length=200, help_text="Pessoa de contato da empresa")
    cliente_cep = models.CharField(max_length=200, help_text="CEP da empresa")
    cliente_rua = models.CharField(max_length=200, help_text="Rua da empresa")
    cliente_numero = models.CharField(max_length=200, help_text="Número da empresa")
    cliente_complemento = models.CharField(max_length=200, help_text="Complamento do endereço da empresa")
    cliente_cidade = models.CharField(max_length=200, help_text="Cidade onde a empresa está localizada")
    cliente_email = models.EmailField(max_length=254, unique="true" , help_text="Email da pessoa de contato da empresa")
    cliente_telefone = models.CharField(max_length=200, help_text="Telefone da empresa")
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
        help_text="Dias de entrega",
    )
    tabela_1 = 'TB1'
    tabela_2 = 'TB2'
    tabela_3 = 'TB3'
    cliente_tabela_opcoes = [
        (tabela_1, 'Tabela 1'),
        (tabela_2, 'Tabela 2'),
        (tabela_3, 'Tabela 3'),
    ]
    cliente_lista_precos = models.CharField(
        max_length = 3,
        choices = cliente_tabela_opcoes,
        help_text="Lista de preços da empresa",
    )
    cliente_ativo = models.BooleanField()
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.cliente_tipo,
            self.cliente_nome_fantasia,
            self.cliente_razao_social,
            self.cliente_nome_contato,
            self.cliente_cep,
            self.cliente_rua,
            self.cliente_numero,
            self.cliente_complemento,
            self.cliente_cidade,
            self.cliente_email,
            self.cliente_telefone,
            self.cliente_dias_entrega,
            self.cliente_lista_precos,
            self.cliente_ativo)