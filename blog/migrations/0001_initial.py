# Generated by Django 2.1.2 on 2018-11-17 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimerNombre', models.CharField(max_length=30)),
                ('SegundoNombre', models.CharField(max_length=30)),
                ('PrimerApellido', models.CharField(max_length=30)),
                ('SegundoApellido', models.CharField(max_length=30)),
                ('Run', models.CharField(max_length=10)),
                ('dv', models.CharField(max_length=1)),
                ('Telefono', models.IntegerField()),
                ('Direccion', models.CharField(max_length=100)),
                ('Comuna', models.CharField(max_length=50)),
                ('Usuario', models.CharField(max_length=50)),
                ('Contraseña', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=200)),
            ],
        ),
    ]
