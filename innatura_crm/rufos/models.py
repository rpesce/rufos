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
    datestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cliente_nome_fantasia

#%s %s %s %s %s %s %s %s %s %s %s %s %s
#            self.cliente_tipo,
#            self.cliente_nome_fantasia,
#           self.cliente_razao_social,
#          self.cliente_nome_contato,
#         self.cliente_cep,
#        self.cliente_rua,
#       self.cliente_numero,
#      self.cliente_complemento,
#            self.cliente_cidade,
#           self.cliente_email,
#          self.cliente_telefone,
#         self.cliente_dias_entrega,
#        self.cliente_lista_precos,
#       self.cliente_ativo

class Produto(models.Model):
    produto_nome = models.CharField(max_length=200, help_text="Nome do produto")
    produto_codigo = models.DecimalField(max_digits=5, decimal_places=2, help_text="Código do produto")
    produto_ncm = models.CharField(max_length=200, help_text="NCM do produto")
    produto_categoria = models.CharField(max_length=200, help_text="Categoria do produto")
    produto_foto = models.ImageField(upload_to = 'uploads/', help_text="Foto do produto")
    produto_un_medida = models.DecimalField(max_digits=3, decimal_places=2, help_text="Unidade de medida do produto")
    origem_propria = 'Prop'
    origem_terceiros = 'Terc'
    produto_origem_opcoes = [
        (origem_propria, 'Própria'),
        (origem_terceiros, 'Terceiros'),
    ]
    produto_origem = models.CharField(
        max_length = 4,
        choices = produto_origem_opcoes,
        help_text="Origem do produto",
    )
    produto_custo = models.DecimalField(max_digits=5, decimal_places=2, help_text="Custo do produto")
    produto_ativo = models.BooleanField()
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produto_nome


class Pedido(models.Model):
    pedido_date = models.DateTimeField(auto_now_add=True)
    pedido_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido_produtos = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pgto_cre = 'Cre'
    pgto_deb = 'Deb'
    pgto_din = 'Din'
    pedido_pgto_opcoes = [
        (pgto_cre, 'Crédito'),
        (pgto_deb, 'Débito'),
        (pgto_din, 'Dinheiro'),
    ]
    pedido_pagamento = models.CharField(
        max_length = 3,
        choices = pedido_pgto_opcoes,
        help_text="Tipo de pagamento",
    )
    pedido_sub_total = models.DecimalField(max_digits=5, decimal_places=2, help_text="Valor total do pedido")
    status_entregue = 'ent'
    status_a_entregar = 'aen'
    status_cancelado = 'can'
    pedido_status_opcoes = [
        (status_entregue, 'Entregue'),
        (status_a_entregar, 'A entregar'),
        (status_cancelado, 'Cancelado'),
    ]
    pedido_status = models.CharField(
        max_length = 3,
        choices = pedido_status_opcoes,
        help_text="Status do pedido",
    )