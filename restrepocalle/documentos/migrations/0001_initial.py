# Generated by Django 3.2.7 on 2024-05-21 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=30, verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreD', models.CharField(max_length=30, verbose_name='Documento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='Archivos/', verbose_name='Archivo')),
                ('observaciones', models.TextField(blank=True, max_length=250)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documentos.cliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documentos.documento')),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'ordering': ['fecha'],
            },
        ),
    ]
