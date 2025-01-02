# inventory/forms.py
from django import forms
from .models import InventoryItem

class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['nama', 'kategori', 'status', 'lokasi', 'gambar', 'kapasitas']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'lokasi': forms.TextInput(attrs={'class': 'form-control'}),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'kapasitas': forms.NumberInput(attrs={'class': 'form-control'}),
        }