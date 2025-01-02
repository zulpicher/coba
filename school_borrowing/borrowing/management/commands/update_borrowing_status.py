# borrowing/management/commands/update_borrowing_status.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from borrowing.models import Borrowing
from notifications.models import Notifikasi

class Command(BaseCommand):
    help = 'Memperbarui status peminjaman dan item setelah end_date terlewati'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        # Mendapatkan peminjaman yang disetujui dan end_date telah lewat
        expired_borrowings = Borrowing.objects.filter(status='approved', end_date__lt=now)
        
        for borrowing in expired_borrowings:
            # Update status peminjaman menjadi 'completed'
            borrowing.status = 'completed'
            borrowing.save()
            
            # Update status item menjadi 'tersedia'
            item = borrowing.item
            item.status = 'tersedia'
            item.save()
            
            # Kirim notifikasi ke siswa
            Notifikasi.objects.create(
                user=borrowing.user,
                pesan=f"Peminjaman Anda untuk {borrowing.item.nama} telah selesai dan item sekarang tersedia kembali."
            )
            
            self.stdout.write(self.style.SUCCESS(
                f"Peminjaman {borrowing.id} oleh {borrowing.user.nama} untuk item {borrowing.item.nama} telah diselesaikan."
            ))
        
        if not expired_borrowings.exists():
            self.stdout.write("Tidak ada peminjaman yang perlu diperbarui.")
