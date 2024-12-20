# Generated by Django 5.1.3 on 2024-12-02 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_autor'),
        ('funcionarios', '0002_funcionario_departamentos_funcionario_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
