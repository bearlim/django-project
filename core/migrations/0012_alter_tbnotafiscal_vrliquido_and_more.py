# Generated by Django 4.0.1 on 2022-01-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_delete_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbnotafiscal',
            name='vrLiquido',
            field=models.FloatField(verbose_name='Valor líquido do Serviço'),
        ),
        migrations.AlterField(
            model_name='tbnotafiscal',
            name='vrServico',
            field=models.FloatField(verbose_name='Valor do Serviço'),
        ),
    ]
