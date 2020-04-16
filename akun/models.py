from django.db import models
from django.utils.translation import gettext_lazy as text

# Create your models here.


class Akun(models.Model):
    nama = models.CharField(max_length=30)
    jenis_kelamin = models.BooleanField(null=True)
    kota_domisili = models.CharField(max_length=30, null=True)
    alamat = models.CharField(max_length=100, null=True)
    tanggal_lahir = models.DateField(null=True)
    tempat_lahir = models.CharField(max_length=30, null=True)
    foto_src = models.TextField(null=True,)
    no_telepon = models.CharField(max_length=16, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    aktif = models.BooleanField(default=True)
    registrasi = models.DateTimeField(auto_now_add=True)
    aktivasi = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class DaftarStatus(models.TextChoices):
        ADMIN = text('admin')
        STAF = text('staf')
        MEMBER = text('member')

    class Meta:
        db_table = 'akun'
    status = models.CharField(max_length=6,
                              choices=DaftarStatus.choices, default=DaftarStatus.MEMBER)

    def __str__(self):
        return self.nama
