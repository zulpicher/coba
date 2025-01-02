# borrowing/forms.py

from django import forms
from .models import Borrowing
from inventory.models import InventoryItem

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['item', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(BorrowingForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = InventoryItem.objects.filter(status='tersedia')

class ProcessBorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['status', 'reason']
        widgets = {
            'status': forms.Select(choices=Borrowing.STATUS_CHOICES),
            'reason': forms.Textarea(attrs={'rows': 3}),
        }
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        reason = cleaned_data.get('reason')

        if status == 'rejected' and not reason:
            self.add_error('reason', 'Alasan wajib diisi ketika peminjaman ditolak.')
        return cleaned_data