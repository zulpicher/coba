# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .decorators import admin_required, siswa_required
from borrowing.models import Borrowing
from inventory.models import InventoryItem
from notifications.models import Notifikasi
from users.models import User

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect('admin_dashboard')
        elif request.user.role == 'siswa':
            return redirect('siswa_dashboard')
    return redirect('login')

def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('siswa_dashboard')
            else:
                form.add_error(None, 'Email atau Password salah')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout_view(request):
    logout(request)
    return redirect('login')

@admin_required
def admin_dashboard(request):
    # **Statistik Peminjaman**
    total_borrowings = Borrowing.objects.count()  # Jumlah seluruh peminjaman
    pending_borrowings = Borrowing.objects.filter(status='pending').count()  # Peminjaman Pending
    approved_borrowings = Borrowing.objects.filter(status='approved').count()  # Peminjaman Diterima
    rejected_borrowings = Borrowing.objects.filter(status='rejected').count()  # Peminjaman Ditolak

    # **Aktivitas Terbaru**
    recent_borrowings = Borrowing.objects.all().order_by('-start_date')[:5]  # 5 peminjaman terbaru
    recent_users = User.objects.all().order_by('-date_joined')[:5]  # 5 pendaftaran user terbaru

    # **Notifikasi**
    admin_notifications = Notifikasi.objects.filter(user__role='admin').order_by('-tanggal_waktu')[:5]  # 5 notifikasi terbaru

    # **Menyusun Context**
    context = {
        'total_borrowings': total_borrowings,
        'pending_borrowings': pending_borrowings,
        'approved_borrowings': approved_borrowings,
        'rejected_borrowings': rejected_borrowings,
        'recent_borrowings': recent_borrowings,
        'recent_users': recent_users,
        'admin_notifications': admin_notifications,
    }

    return render(request, 'users/admin_dashboard.html', context)

@siswa_required
def siswa_dashboard(request):
    # Menampilkan peminjaman terbaru yang dilakukan oleh siswa
    latest_borrowings = Borrowing.objects.filter(user=request.user).order_by('-start_date')[:5]
    # Menampilkan semua item, baik tersedia maupun dipinjam
    all_items = InventoryItem.objects.all().order_by('nama')
    context = {
        'latest_borrowings': latest_borrowings,
        'all_items': all_items,
    }
    return render(request, 'users/siswa_dashboard.html', context)
