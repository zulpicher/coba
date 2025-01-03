# Generated by Django 5.1.4 on 2024-12-31 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('status', models.CharField(choices=[('tersedia', 'Tersedia'), ('dipinjam', 'Dipinjam')], default='tersedia', max_length=10)),
                ('lokasi', models.CharField(max_length=255)),
                ('gambar', models.ImageField(upload_to='inventory_images/')),
                ('kapasitas', models.IntegerField(blank=True, null=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.kategori')),
            ],
        ),
    ]
