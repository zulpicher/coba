# borrowing/admin.py

from django.contrib import admin
from .models import Borrowing

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'item', 'user')
    search_fields = ('user__nama', 'item__nama')
