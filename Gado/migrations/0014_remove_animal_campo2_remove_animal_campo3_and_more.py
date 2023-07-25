# Generated by Django 4.1 on 2023-07-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gado', '0013_alter_animal_lote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='campo2',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='campo3',
        ),
        migrations.AlterField(
            model_name='animal',
            name='campo1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gado.fornecedor'),
        ),
    ]