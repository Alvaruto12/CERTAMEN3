# Generated by Django 4.2.6 on 2023-11-28 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('C', 'Comunidad USM'), ('E', 'Estudiante'), ('P', 'Profesor'), ('J', 'Jefe de Carrera')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('I', 'Info'), ('V', 'Vacaciones'), ('F', 'Feriado'), ('SA', 'Suspension de actividades'), ('SAPM', 'Suspension de actividades PM'), ('PL', 'Periodo Lectivo'), ('SE', 'Suspension de Evaluaciones'), ('C', 'Ceremonia'), ('ED', 'EDDA'), ('EV', 'Evaluacion'), ('A', 'Ayudantias'), ('HA', 'Hito Academico'), ('SA', 'Secretaria Academica'), ('OA', 'OAI')], default='I', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.segmento')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.tipo')),
            ],
        ),
    ]