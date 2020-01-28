# Generated by Django 3.0 on 2020-01-28 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rufos', '0009_auto_20200127_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='pedido_produtos',
        ),
        migrations.AddField(
            model_name='pedidoproduto',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rufos.Pedido'),
            preserve_default=False,
        ),
    ]
