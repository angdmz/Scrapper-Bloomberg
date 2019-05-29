# Generated by Django 2.1.3 on 2018-11-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'verbose_name': 'Cotizacion', 'verbose_name_plural': 'Cotizaciones'},
        ),
        migrations.AlterModelOptions(
            name='fondo',
            options={'verbose_name': 'Fondo de inversion', 'verbose_name_plural': 'Fondos de inversion'},
        ),
        migrations.AddField(
            model_name='fondo',
            name='codigo',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
