# Generated by Django 5.1.3 on 2024-11-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodcutos',
            fields=[
                ('id_producto', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('olor', models.CharField(max_length=50)),
                ('gramos', models.CharField(max_length=50)),
                ('uso', models.CharField(max_length=50)),
                ('precio', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
