# Generated by Django 2.1.3 on 2018-11-29 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cotizacion',
            },
        ),
        migrations.CreateModel(
            name='Fondo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=120)),
            ],
            options={
                'db_table': 'fondo',
            },
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='fondo',
            field=models.ForeignKey(db_column='fondo_id', on_delete=django.db.models.deletion.CASCADE, to='fondos.Fondo'),
        ),
    ]