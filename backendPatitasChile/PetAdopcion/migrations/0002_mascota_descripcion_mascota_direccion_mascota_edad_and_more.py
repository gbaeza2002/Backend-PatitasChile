# Generated by Django 4.2.3 on 2024-11-15 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PetAdopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='descripcion',
            field=models.CharField(default='Sin descripción', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='edad',
            field=models.CharField(default='Sin dirección', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adopcion',
            name='fechaAdopcion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
