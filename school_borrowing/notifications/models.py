# notifications/models.py
from django.db import models
from users.models import User

class Notifikasi(models.Model):
    STATUS_CHOICES = (
        ('terkirim', 'Terkirim'),
        ('dibaca', 'Dibaca'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pesan = models.TextField()
    tanggal_waktu = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='terkirim')
    reason = models.TextField(null=True, blank=True)  # Field baru untuk alasan
    tanggal_waktu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notifikasi untuk {self.user.nama} - {self.status}"  
