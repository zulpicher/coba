# borrowing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_borrowing, name='submit_borrowing'),
    path('admin/list/', views.borrowing_list, name='borrowing_list'),
    path('admin/process/<int:borrowing_id>/', views.process_borrowing, name='process_borrowing'),
    path('history/', views.borrowing_history, name='borrowing_history'),
]
