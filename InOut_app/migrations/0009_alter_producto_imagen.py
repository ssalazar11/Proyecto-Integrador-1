# Generated by Django 4.1 on 2022-09-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InOut_app', '0008_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Imagen',
            field=models.ImageField(default='static/images/pan.png', upload_to=''),
        ),
    ]
