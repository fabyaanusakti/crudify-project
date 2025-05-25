from django import forms
from .models import ProjekModels

class ProjekForm(forms.ModelForm):
    class Meta:
        model = ProjekModels
        fields = '__all__'
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
            'deskripsi': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nama_projek': 'Nama Projek',
            'deskripsi': 'Deskripsi',
            'lokasi': 'Lokasi',
            'tanggal_mulai': 'Tanggal Mulai',
            'tanggal_selesai': 'Tanggal Selesai',
            'supervisor': 'Supervisor',
            'status_projek': 'Status Projek',
        }