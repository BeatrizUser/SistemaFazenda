# Generated by Django 4.1 on 2023-07-25 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raca',
            options={'verbose_name_plural': 'Raças'},
        ),
        migrations.RemoveField(
            model_name='animal',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='medicamento',
            name='keysanidade',
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='classificacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gado.classificacaosanidade'),
        ),
    ]
