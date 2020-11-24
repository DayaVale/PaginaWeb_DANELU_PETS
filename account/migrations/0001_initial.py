# Generated by Django 3.1.2 on 2020-11-24 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('cedula_admin', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-cedula_admin',),
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('id_producto', models.CharField(max_length=200)),
                ('cantidad_producto', models.SmallIntegerField()),
                ('total_producto', models.IntegerField()),
            ],
            options={
                'ordering': ('-id_carrito', '-id_producto'),
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-especie',),
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-nombre1', '-apellido1'),
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('numero_cuenta', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('valor_total', models.IntegerField()),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.carrito')),
            ],
            options={
                'ordering': ('-numero_cuenta', '-valor_total'),
            },
        ),
        migrations.CreateModel(
            name='Domiciliario',
            fields=[
                ('id_domiciliario', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=50)),
                ('nombre2', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('medio_transporte', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-id_domiciliario', '-medio_transporte'),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio_producto', models.IntegerField()),
                ('precio_produccion', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
                ('especificaciones', models.CharField(default=None, max_length=1000)),
                ('admin_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.admin')),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.categoria')),
            ],
            options={
                'ordering': ('-precio_producto', '-nombre_producto'),
            },
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id_domicilio', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('metodo_de_pago', models.CharField(max_length=50)),
                ('id_domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.domiciliario')),
                ('numero_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.cuenta')),
            ],
            options={
                'ordering': ('-id_domicilio', '-id_domiciliario'),
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='id_cliente',
            field=models.ManyToManyField(to='account.Cliente'),
        ),
    ]