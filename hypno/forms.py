from django import forms
from .models import PaketTerapi, Audio
import datetime


class PaketTerapiForm(forms.ModelForm):
    nama = forms.CharField()
    deskripsi = forms.CharField(widget=forms.Textarea)
    harga = forms.IntegerField()
    aktif = forms.ChoiceField(widget=forms.RadioSelect)
    mulai = forms.DateField(initial=datetime.date.today)
    akhir = forms.DateField(initial=datetime.date.today)

    nama.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Paket Terapi.'
    })
    deskripsi.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Deskripsi Paket Terapi',
        'rows': 4
    })
    harga.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Harga Paket'
    })
    mulai.widget.attrs.update({
        'class': 'form-control',
        'type': 'date',
        'placeholder': 'Mulai langganan Paket',
        'id': 'id_mulai',
    })
    akhir.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Selesai langganan Paket',
        'id': 'id_akhir',
    })
    aktif.widget.choices = [
        (True, 'Ya'),
        (False, 'Tidak')
    ]

    class Meta:
        model = PaketTerapi
        fields = ['nama', 'deskripsi', 'harga', 'aktif', 'mulai', 'akhir']


class AudioForm(forms.ModelForm):
    nama = forms.CharField()
    keterangan = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()
    nama.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Paket Terapi.'
    })
    keterangan.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Deskripsi Paket Terapi',
        'rows': 4
    })
    file.widget.attrs.update({
        'class': 'btn btn-secondary btn-sm'
    })

    class Meta:
        model = Audio
        fields = ['nama', 'keterangan', 'file']
