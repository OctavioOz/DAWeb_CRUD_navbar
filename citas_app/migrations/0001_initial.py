# Generated by Django 5.1 on 2024-11-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id_cita', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_cliente', models.PositiveSmallIntegerField()),
                ('id_trabajador', models.PositiveSmallIntegerField()),
                ('fecha_cita', models.DateField()),
                ('id_corte', models.PositiveSmallIntegerField()),
                ('total', models.CharField(max_length=50)),
            ],
        ),
    ]
