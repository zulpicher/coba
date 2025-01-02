# borrowing/models.py

from django.db import models
from users.models import User
from inventory.models import InventoryItem

class Borrowing(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Diterima'),
        ('rejected', 'Ditolak'),
        ('completed', 'Selesai'),  # Tambahkan ini
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowings')
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='borrowings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.nama} - {self.item.nama} ({self.status})"
