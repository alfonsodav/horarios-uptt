# Generated by Django 3.0.4 on 2020-03-18 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pnf',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='secciones',
            name='trayecto',
        ),
        migrations.AddField(
            model_name='horarios',
            name='codigo',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='secciones',
            name='horarios',
            field=models.ManyToManyField(to='horario.Horarios'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='codigo',
            field=models.CharField(max_length=10, verbose_name='Codigo de Materia'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre de Materia'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='unidadesC',
            field=models.IntegerField(verbose_name='Unidades Curriculares'),
        ),
        migrations.RemoveField(
            model_name='secciones',
            name='pnf',
        ),
        migrations.AddField(
            model_name='secciones',
            name='pnf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='horario.PNF'),
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('materias', models.ManyToManyField(to='horario.Materias')),
            ],
        ),
        migrations.AddField(
            model_name='pnf',
            name='trimetres',
            field=models.ManyToManyField(to='horario.Trimestre'),
        ),
        migrations.AlterField(
            model_name='secciones',
            name='trimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='horario.Trimestre'),
        ),
    ]
