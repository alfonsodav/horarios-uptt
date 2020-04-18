# Generated by Django 3.0.4 on 2020-04-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0006_auto_20200330_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('pnf', models.ManyToManyField(null=True, related_name='pnf', to='horario.PNF')),
            ],
        ),
    ]
