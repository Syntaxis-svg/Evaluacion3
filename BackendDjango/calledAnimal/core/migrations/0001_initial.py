# Generated by Django 4.0.4 on 2022-06-07 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
    ]
