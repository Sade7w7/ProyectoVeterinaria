# Generated by Django 4.2 on 2023-05-09 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto_cantidad', models.CharField(db_column='nombre_producto-cantidad', max_length=500)),
                ('fecha', models.DateTimeField()),
                ('valor', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_mascota', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('caracteristicas', models.CharField(max_length=50)),
                ('peso', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('medicamento_dosis', models.CharField(db_column='medicamento-dosis', max_length=500)),
            ],
            options={
                'db_table': 'orden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula_persona', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_persona', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=3)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('contraseña', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro', primary_key=True, serialize=False)),
                ('motivo', models.CharField(db_column='Motivo', max_length=500)),
                ('sintomatologia', models.CharField(blank=True, db_column='Sintomatologia', max_length=500, null=True)),
                ('diagnostico', models.CharField(db_column='Diagnostico', max_length=500)),
                ('procedimiento', models.CharField(blank=True, db_column='Procedimiento', max_length=100, null=True)),
                ('detalle_procedimiento', models.CharField(blank=True, db_column='Detalle_Procedimiento', max_length=500, null=True)),
                ('historial_vacunacion', models.CharField(blank=True, db_column='Historial_Vacunacion', max_length=500, null=True)),
            ],
            options={
                'db_table': 'registro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_rol', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialClinico',
            fields=[
                ('id_mascota', models.OneToOneField(db_column='id_mascota', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='AppVeterinaria.mascota')),
            ],
            options={
                'db_table': 'historial_clinico',
                'managed': False,
            },
        ),
    ]
