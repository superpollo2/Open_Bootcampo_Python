# Generated by Django 4.1.1 on 2022-10-12 05:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id_director', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('born_date', models.DateField(default=datetime.date.today)),
                ('city_born', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id_pelicula', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('productora', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=20)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cineastas.director')),
            ],
        ),
    ]