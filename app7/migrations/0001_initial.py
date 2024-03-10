# Generated by Django 5.0.3 on 2024-03-10 18:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitalizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hospitalizacion', models.IntegerField()),
                ('nombre_paciente', models.CharField(max_length=512)),
                ('edad', models.IntegerField()),
                ('motivo', models.CharField(max_length=512)),
                ('pais_origen', models.CharField(max_length=512)),
                ('idioma', models.CharField(choices=[('es', 'Español'), ('en', 'English')], max_length=512)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('no_visitas', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]