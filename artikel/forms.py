from django import forms
import datetime
from .models import Artikel, Komentar


class ArtikelForm(forms.ModelForm):
    ikon_src = forms.CharField(widget=forms.HiddenInput, required=False)
    judul = forms.CharField()
    penulis = forms.CharField()
    konten = forms.CharField(widget=forms.Textarea, required=False)
    aktif = forms.ChoiceField(widget=forms.RadioSelect, initial=True)

    judul.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Judul Artikel'
    })
    penulis.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Penulis'
    })
    konten.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Deskripsi isi artikel',
        'rows': 4
    })
    aktif.widget.attrs.update({
        'class': 'form-check-input',
    })
    aktif.widget.choices = [
        (True, 'Ya'),
        (False, 'Tidak')
    ]

    class Meta:
        model = Artikel
        fields = ['ikon_src', 'judul', 'penulis', 'konten', 'aktif']


class KomentarForm(forms.ModelForm):
    konten = forms.CharField(widget=forms.Textarea)
    konten.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Deskripsi isi Komentar',
        'rows': 4
    })

    class Meta:
        model = Komentar
        fields = ['konten']
