# Generated by Django 3.2.4 on 2022-10-30 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre'], 'verbose_name': 'Departamentos', 'verbose_name_plural': 'Departamentos'},
        ),
    ]