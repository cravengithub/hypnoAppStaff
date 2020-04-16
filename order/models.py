from django.db import models
from akun.models import Akun
from hypno.models import PaketTerapi
from django.utils.translation import gettext_lazy as text


# Create your models here.


class Order(models.Model):
    pesan = models.DateTimeField(auto_now_add=True)
    bukti_path = models.TextField()
    tanggal_bayar = models.DateTimeField()
    rek_pemesan = models.CharField(max_length=100)
    bank_pemesan = models.CharField(max_length=100)
    an_pemesan = models.CharField(max_length=100)
    rek_tujuan = models.CharField(max_length=100)
    bank_tujuan = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    member = models.ForeignKey(
        Akun, related_name='order', on_delete=models.CASCADE)
    paket_terapi = models.ForeignKey(
        PaketTerapi, related_name='order', on_delete=models.CASCADE)

    class DaftarStatus(models.TextChoices):
        KONFIRMASI = text('konfirmasi')
        PESAN = text('pesan')
        AKTIF = text('aktif')

    class Meta:
        db_table = 'order'
    status = models.CharField(max_length=12,
                              choices=DaftarStatus.choices, default=DaftarStatus.PESAN)
