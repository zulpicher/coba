# Generated by Django 5.1.4 on 2024-12-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='stok',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='tipe',
            field=models.CharField(choices=[('barang', 'Barang'), ('ruangan', 'Ruangan')], default='barang', max_length=10),
        ),
    ]
