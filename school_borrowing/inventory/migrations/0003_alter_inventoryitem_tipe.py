# Generated by Django 5.1.4 on 2025-01-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventoryitem_stok_inventoryitem_tipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='tipe',
            field=models.CharField(choices=[('barang', 'Barang'), ('ruangan', 'Ruangan')], max_length=10),
        ),
    ]
