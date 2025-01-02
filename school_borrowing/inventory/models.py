# inventory/models.py

from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class InventoryItem(models.Model):
    STATUS_CHOICES = (
        ('tersedia', 'Tersedia'),
        ('dipinjam', 'Dipinjam'),
    )
    
    TYPING_CHOICES = (
        ('barang', 'Barang'),
        ('ruangan', 'Ruangan'),
    )

    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='tersedia')
    lokasi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='inventory_images/')
    kapasitas = models.IntegerField(null=True, blank=True)  # Hanya untuk ruangan
    
    def __str__(self):
        return self.nama
