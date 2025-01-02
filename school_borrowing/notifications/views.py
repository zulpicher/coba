# notifications/views.py

from django.shortcuts import render, get_object_or_404, redirect
from users.decorators import admin_required, siswa_required
from .models import Notifikasi
from django.contrib.auth.decorators import login_required  # Tambahkan jika diperlukan

@admin_required
def notifikasi_admin(request):
    notifications = Notifikasi.objects.filter(user__role='admin').order_by('-tanggal_waktu')
    return render(request, 'notifications/notifikasi_admin.html', {'notifications': notifications})

@siswa_required
def notifikasi_siswa(request):
    notifications = Notifikasi.objects.filter(user=request.user).order_by('-tanggal_waktu')
    return render(request, 'notifications/notifikasi_siswa.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notifikasi, id=notification_id, user=request.user)
    if notification.status != 'dibaca':
        notification.status = 'dibaca'
        notification.save()
    
    # Redirect berdasarkan role pengguna
    if request.user.role == 'admin':
        return redirect('notifikasi_admin')
    else:
        return redirect('notifikasi_siswa')
