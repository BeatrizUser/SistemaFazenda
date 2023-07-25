# Generated by Django 4.1 on 2023-07-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gado', '0009_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endereco',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
