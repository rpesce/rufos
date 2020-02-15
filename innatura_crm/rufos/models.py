from django.db import models

# Create your models here.

class Entrega(models.Model):
    segunda = 'SEG'
    terca = 'TER'
    quarta = 'QUA'
    quinta = 'QUI'
    sexta = 'SEX'
    sabado = 'SAB'
    domingo = 'DOM'
    entrega_opcoes = [
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
        choices = entrega_opcoes,
    )
    
    def __str__(self):
        return self.cliente_dias_entrega

class Cliente(models.Model):
    pessoa_fisica = 'FIS'
    pessoa_juridica = 'JUR'
    cliente_tipo_opcoes = [
        (pessoa_fisica, 'Pessoa Física'),
        (pessoa_juridica, 'Pessoa Jurídica'),
    ]
    cliente_tipo = models.CharField(
        verbose_name="tipo",
        max_length = 3,
        choices = cliente_tipo_opcoes,
    )
    cliente_nome_fantasia = models.CharField(verbose_name="nome fantasia", max_length=200)
    cliente_razao_social = models.CharField(verbose_name="razão social", max_length=200)
    cliente_rua = models.CharField(verbose_name="rua", max_length=200)
    cliente_numero = models.CharField(verbose_name="número", max_length=200)
    cliente_complemento = models.CharField(verbose_name="complemento", max_length=200)
    cliente_cep = models.CharField(verbose_name="CEP",max_length=200, help_text="Exemplo: 00000-000")
    cliente_cidade = models.CharField(verbose_name="cidade", max_length=200)
    cliente_nome_contato = models.CharField(verbose_name="pessoa de contato", max_length=200)
    cliente_email = models.EmailField(verbose_name="email de contato", max_length=254, unique="true")
    cliente_telefone = models.CharField(verbose_name="telefone de contato", max_length=200, help_text="Exemplo: 51 9 0000 0000")
    cliente_dias_entrega = models.ManyToManyField(
        Entrega,
        verbose_name="dias de entrega",
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
        verbose_name="tabela de preços",
    )
    cliente_ativo = models.BooleanField(default=True)
    datestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cliente_nome_fantasia

class Produto(models.Model):
    produto_nome = models.CharField(verbose_name="produto", max_length=200)
    produto_codigo = models.DecimalField(verbose_name="código", max_digits=5, decimal_places=2)
    produto_ncm = models.CharField(verbose_name="NCM", max_length=200)
    produto_categoria = models.CharField(verbose_name="categoria", max_length=200)
    produto_foto = models.ImageField(upload_to = 'uploads/', verbose_name="foto")
    produto_un_medida = models.DecimalField(verbose_name="unidade de medida", max_digits=3, decimal_places=2, help_text="Unidade em kilograma")
    origem_propria = 'Prop'
    origem_terceiros = 'Terc'
    produto_origem_opcoes = [
        (origem_propria, 'Própria'),
        (origem_terceiros, 'Terceiros'),
    ]
    produto_origem = models.CharField(
        max_length = 4,
        choices = produto_origem_opcoes,
        verbose_name="origem",
    )
    produto_preco_tb1 = models.DecimalField(verbose_name="preço tabela 1", max_digits=5, decimal_places=2, default=0.00)
    produto_preco_tb2 = models.DecimalField(verbose_name="preço tabela 2", max_digits=5, decimal_places=2, default=0.00)
    produto_preco_tb3 = models.DecimalField(verbose_name="preço tabela 3", max_digits=5, decimal_places=2, default=0.00)
    produto_custo = models.DecimalField(verbose_name="preço custo", max_digits=5, decimal_places=2, default=0.00)
    produto_ativo = models.BooleanField(verbose_name="produto ativo", default=True)
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produto_nome

class Pedido(models.Model):
    pedido_date = models.DateTimeField(verbose_name="data", auto_now_add=True)
    pedido_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="cliente")
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
        verbose_name="tipo de pagamento",
    )
    status_entregue = 'Entregue'
    status_confirmado = 'Confirmado'
    status_cancelado = 'Cancelado'
    pedido_status_opcoes = [
        (status_entregue, 'Entregue'),
        (status_confirmado, 'Confirmado'),
        (status_cancelado, 'Cancelado'),
    ]
    pedido_status = models.CharField(
        max_length = 10,
        choices = pedido_status_opcoes,
        verbose_name="status",
        default= status_confirmado,
    )
    pedido_sub_total = models.DecimalField(verbose_name="sub total", max_digits=5, decimal_places=2, default=1)

    def __str__(self):
        return '%s' % (self.pedido_cliente.cliente_nome_fantasia)


class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '%s' % (self.pedido.pedido_cliente)

    """@property
    def get_price(self, produto):
        self.tabela = self.pedido.pedido_cliente.cliente_lista_precos
        return self.tabela


        def valor_tt(self, pedido):
        self.tabela = self.pedido.pedido_cliente.cliente_lista_precos
        print(tabela)
        
         , quantidade, produto if tabela == "TB1":
            self.valor_total = self.quantidade * self.produto.produto_preco_tb1
        elif tabela == "TB2":
            self.valor_total = self.quantidade * self.produto.produto_preco_tb2
        elif tabela == "TB3":
            self.valor_total = self.quantidade * self.produto.produto_preco_tb3
        return self.valor_total"""