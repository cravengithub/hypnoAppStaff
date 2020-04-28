from django import forms
import datetime
from .models import Akun


class AkunForm(forms.ModelForm):

    nama = forms.CharField()
    foto_src = forms.CharField(widget=forms.HiddenInput, required=False)
    kota_domisili = forms.CharField()
    alamat = forms.CharField(widget=forms.Textarea, required=False)
    jenis_kelamin = forms.ChoiceField(widget=forms.RadioSelect)
    aktif = forms.ChoiceField(widget=forms.RadioSelect)
    tanggal_lahir = forms.DateField(initial=datetime.date.today)
    email = forms.EmailField()
    tempat_lahir = forms.CharField()
    no_telepon = forms.IntegerField(min_value=10)
    status = forms.ChoiceField(widget=forms.Select)
    verification_code = forms.IntegerField(disabled=True)
    verification = forms.ChoiceField(widget=forms.Select)

    nama.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nama lengkap.'
    })
    kota_domisili.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Kota yang ditempati sekarang.'
    })
    alamat.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Alamat tempat tinggal sekarang.',
        'rows': 4
    })
    email.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Alamat Email.'
    })
    tempat_lahir.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Tempat Lahir.'
    })
    no_telepon.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Nomor Telepon/Handphone.'
    })
    status.widget.attrs.update({
        'class': 'form-control', 'placeholder': 'Status Akun'
    })
    status.choices = [
        ('admin', 'Admin'),
        ('staf', 'Staf'),
        ('member', 'Member'),
    ]

    jenis_kelamin.widget.attrs.update({
        'class': 'form-check-input',
    })
    jenis_kelamin.widget.choices = [
        (False, 'Perempuan'),
        (True, 'Laki-laki')
    ]
    aktif.widget.attrs.update({
        'class': 'form-check-input',
    })
    aktif.widget.choices = [
        (True, 'Ya'),
        (False, 'Tidak')
    ]
    verification.choices = [
        (True, 'Ya'),
        (False, 'Tidak')
    ]

    tanggal_lahir.widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Tanggal Lahir.',
        'id': 'id_tanggal_lahir',
    })

    class Meta:
        model = Akun
        fields = ['nama', 'foto_src', 'kota_domisili', 'alamat', 'tanggal_lahir',
                  'jenis_kelamin', 'aktif', 'email', 'tempat_lahir', 'no_telepon', 'status', 'verification_code']
