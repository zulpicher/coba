# borrowing/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Borrowing
from .forms import BorrowingForm, ProcessBorrowingForm
from users.decorators import admin_required, siswa_required
from notifications.models import Notifikasi
from users.models import User
from django.contrib import messages

@siswa_required
def submit_borrowing(request):
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            borrowing = form.save(commit=False)
            borrowing.user = request.user
            # Cek konflik jadwal
            item = borrowing.item
            if not check_conflict(item, borrowing.start_date, borrowing.end_date):
                borrowing.save()
                # Kirim notifikasi ke semua admin
                admins = User.objects.filter(role='admin')
                for admin in admins:
                    Notifikasi.objects.create(
                        user=admin,
                        pesan=f"Permohonan borrowing dari {request.user.nama} untuk {item.nama}."
                    )
                messages.success(request, 'Permohonan borrowing berhasil diajukan.')
                return redirect('borrowing_history')
            else:
                form.add_error(None, 'Konflik jadwal. Silakan pilih waktu lain.')
    else:
        form = BorrowingForm()
    return render(request, 'borrowing/submit_borrowing.html', {'form': form})

@admin_required
def borrowing_list(request):
    borrowings = Borrowing.objects.all().order_by('-start_date')
    return render(request, 'borrowing/borrowing_list.html', {'borrowings': borrowings})

@admin_required
def process_borrowing(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)

    if request.method == 'POST':
        form = ProcessBorrowingForm(request.POST, instance=borrowing)
        if form.is_valid():
            borrowing = form.save()

            # Update item status jika disetujui
            if borrowing.status == 'approved':
                borrowing.item.status = 'dipinjam'
                borrowing.item.save()
            elif borrowing.status == 'rejected':
                borrowing.item.status = 'tersedia'  # Asumsikan item menjadi tersedia kembali

            # Kirim notifikasi ke siswa dengan alasan jika ada
            Notifikasi.objects.create(
                user=borrowing.user,
                pesan=f"Permohonan borrowing Anda untuk {borrowing.item.nama} telah {borrowing.get_status_display().lower()}.",
                reason=borrowing.reason  # Sertakan alasan
            )

            # Tambahkan pesan berdasarkan status
            if borrowing.status == 'approved':
                messages.success(request, 'Permohonan borrowing telah disetujui.')
            elif borrowing.status == 'rejected':
                messages.warning(request, 'Permohonan borrowing telah ditolak.')

            return redirect('borrowing_list')
    else:
        form = ProcessBorrowingForm(instance=borrowing)

    return render(request, 'borrowing/process_borrowing.html', {'form': form, 'borrowing': borrowing})

@siswa_required
def borrowing_history(request):
    borrowings = Borrowing.objects.filter(user=request.user).order_by('-start_date')
    print(f"Borrowings for user {request.user.nama}: {borrowings}")  # Debugging
    return render(request, 'borrowing/borrowing_history.html', {'borrowings': borrowings})

def check_conflict(item, start, end):
    conflicts = Borrowing.objects.filter(
        item=item,
        status='approved',
        start_date__lt=end,
        end_date__gt=start
    )
    return conflicts.exists()

