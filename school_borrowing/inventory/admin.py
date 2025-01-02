# inventory/admin.py

from django.contrib import admin
from .models import Kategori, InventoryItem

admin.site.register(Kategori)
admin.site.register(InventoryItem)
