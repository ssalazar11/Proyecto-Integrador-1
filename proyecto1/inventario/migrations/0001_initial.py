# Generated by Django 4.0.6 on 2022-08-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=120)),
                ('usuario', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
            ],
        ),
    ]
