from django import forms
import datetime
from hypno.models import PaketTerapi
from .models import Order


# Kelas ini tidak jadi digunakan.
class PencarianForm(forms.ModelForm):
    email = forms.EmailField()
    status = forms.ChoiceField(widget=forms.Select)
    paket_terapi = forms.ChoiceField(widget=forms.Select)
    email.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Alamat Email.'
    })
    status.choices = [
        ('konfirmasi', 'KONFIRMASI'),
        ('pesan', 'PESAN'),
        ('aktif', 'AKTIF'),
    ]


class OrderForm(forms.ModelForm):
    tanggal_bayar = forms.DateField(initial=datetime.date.today)
    bukti_path = forms.CharField(widget=forms.HiddenInput)
    rek_pemesan = forms.CharField(max_length=100)
    bank_pemesan = forms.CharField(max_length=100)
    an_pemesan = forms.CharField(max_length=100)
    rek_tujuan = forms.CharField(max_length=100)
    bank_tujuan = forms.CharField(max_length=100)
    jumlah = forms.IntegerField(min_value=1)
    email = forms.EmailField()
    paket_terapi = forms.ChoiceField(widget=forms.Select)
    status = forms.ChoiceField(widget=forms.Select)

    tanggal_bayar.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Tanggal Lahir.',
        'id': 'id_tanggal_bayar',
    })

    rek_pemesan.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nomor Rekening Pemesan.'
    })

    bank_pemesan.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Bank Pemesan.'
    })

    an_pemesan.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Pemilik Rekening Bank Pemesan.'
    })

    rek_tujuan.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nomor Rekening Bank yang dituju.'
    })

    bank_tujuan.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama Bank yang dituju.'
    })

    jumlah.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Jumlah pembayaran yang telah dibayarkan.'
    })

    email.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Alamat Email.'
    })
    paket_terapi.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Daftar Paket Terapi'
    })
    paket_terapi.widget.choices = [
        (pt.id, pt.nama) for pt in PaketTerapi.objects.all()
    ]
    status.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Status Pemesanan'
    })
    status.choices = [
        ('konfirmasi', 'Konfirmasi'),
        ('pesan', 'Pesan'),
        ('aktif', 'Aktif'),
    ]

    class Meta:
        model = Order
        fields = ['tanggal_bayar', 'bukti_path', 'rek_pemesan', 'bank_pemesan',
                  'an_pemesan', 'rek_tujuan', 'bank_tujuan', 'jumlah', 'status']
