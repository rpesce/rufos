# Generated by Django 3.0 on 2020-01-27 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rufos', '0007_auto_20200126_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidoproduto',
            old_name='produto_quantidade',
            new_name='quantidade',
        ),
        migrations.RemoveField(
            model_name='pedidoproduto',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedidoproduto',
            name='pedido_item_preco',
        ),
        migrations.AddField(
            model_name='pedido',
            name='pedido_produtos',
            field=models.ManyToManyField(to='rufos.PedidoProduto'),
        ),
        migrations.AlterField(
            model_name='pedidoproduto',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rufos.Produto'),
            preserve_default=False,
        ),
    ]