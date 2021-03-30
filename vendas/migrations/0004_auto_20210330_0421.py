# Generated by Django 3.1.7 on 2021-03-30 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_cliente_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='email_cliente',
        ),
        migrations.AddField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendas.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(to='vendas.Produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor do produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='comprovante_venda',
            field=models.FileField(upload_to='comprovante_venda/', verbose_name='Comprovante de Venda'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Codigo do contrato'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='numero_venda',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número da Venda'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='qtd_itens',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantidade de Itens Vendidos'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor total da venda'),
        ),
    ]
