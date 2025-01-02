# inventory/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem
from .forms import InventoryForm
from users.decorators import admin_required
from django.contrib import messages

@admin_required
def add_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item berhasil ditambahkan.')
            return redirect('inventory_list')
        else:
            messages.error(request, 'Terjadi kesalahan saat menambahkan item. Silakan periksa kembali.')
    else:
        form = InventoryForm()
    return render(request, 'inventory/add_item.html', {'form': form})


@admin_required
def edit_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form})

@admin_required
def delete_item(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/delete_item.html', {'item': item})

@admin_required
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})
