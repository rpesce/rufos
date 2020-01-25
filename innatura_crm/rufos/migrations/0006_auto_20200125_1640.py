# Generated by Django 3.0 on 2020-01-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rufos', '0005_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_dias_entrega', models.CharField(choices=[('SEG', 'Segunda-Feira'), ('TER', 'Terça-Feira'), ('QUA', 'Quarta-Feira'), ('QUI', 'Quinta-Feira'), ('SEX', 'Sexta-Feira'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], help_text='Dias de entrega', max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='pedido_produtos',
        ),
        migrations.AddField(
            model_name='produto',
            name='produto_preco_tb1',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Preço Tabela 1', max_digits=5),
        ),
        migrations.AddField(
            model_name='produto',
            name='produto_preco_tb2',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Preço Tabela 2', max_digits=5),
        ),
        migrations.AddField(
            model_name='produto',
            name='produto_preco_tb3',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Preço Tabela 3', max_digits=5),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_cep',
            field=models.CharField(help_text='00000-000', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_cidade',
            field=models.CharField(help_text='Cidade', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_complemento',
            field=models.CharField(help_text='Complemento', max_length=200),
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cliente_dias_entrega',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_email',
            field=models.EmailField(help_text='Email para contato', max_length=254, unique='true'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_nome_contato',
            field=models.CharField(help_text='Pessoa de contato', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_nome_fantasia',
            field=models.CharField(help_text='Nome Fantasia', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_numero',
            field=models.CharField(help_text='Número', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_razao_social',
            field=models.CharField(help_text='Razão social', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_rua',
            field=models.CharField(help_text='Nome da rua', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_telefone',
            field=models.CharField(help_text='Telefone', max_length=200),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pedido_status',
            field=models.CharField(choices=[('ent', 'Entregue'), ('aen', 'A entregar'), ('can', 'Cancelado')], default='aen', help_text='Status do pedido', max_length=3),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_custo',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Custo do produto', max_digits=5),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cliente_dias_entrega',
            field=models.ManyToManyField(related_name='dias_entrega', to='rufos.Entrega'),
        ),
    ]