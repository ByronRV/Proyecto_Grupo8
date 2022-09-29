# Generated by Django 4.1.1 on 2022-09-28 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_pro', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=10, verbose_name='Color')),
                ('precio', models.IntegerField(default=0)),
                ('talla', models.CharField(max_length=3, unique=True, verbose_name='Talla')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_car', models.AutoField(primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField(default=0)),
                ('prendas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='aplicacion.productos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
