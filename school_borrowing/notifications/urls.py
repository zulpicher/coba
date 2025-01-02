# notifications/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.notifikasi_admin, name='notifikasi_admin'),
    path('siswa/', views.notifikasi_siswa, name='notifikasi_siswa'),
    path('mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]
