# Generated by Django 3.2.3 on 2022-10-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20221031_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='numero',
            field=models.CharField(max_length=10),
        ),
    ]
