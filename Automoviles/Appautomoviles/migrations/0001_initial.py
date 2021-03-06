# Generated by Django 4.0.5 on 2022-06-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo')),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Sedan'), (2, 'Suv'), (3, 'Hatchback'), (4, 'Deportivos'), (5, 'Van'), (6, 'Pick up')], verbose_name='Tipo')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
            options={
                'verbose_name_plural': 'Automoviles',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('cuil', models.CharField(max_length=13, verbose_name='CUIL')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Personal',
            },
        ),
    ]
