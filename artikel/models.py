from django.db import models
from akun.models import Akun
from django.utils.translation import gettext_lazy as text

# Create your models here.


class Artikel(models.Model):
    ikon_src = models.TextField(null=True)
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100, null=True)
    konten = models.TextField(null=True)
    aktif = models.BooleanField(default=True)
    publikasi = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'artikel'

    def __str__(self):
        return self.judul


class Komentar(models.Model):
    artikel = models.ForeignKey(
        Artikel, related_name='komentar', on_delete=models.CASCADE)
    member = models.ForeignKey(
        Akun, related_name='komentar', on_delete=models.CASCADE, )
    konten = models.TextField(null=True)
    publikasi = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    aktif = models.BooleanField(default=True)

    class Meta:
        db_table = 'komentar'

    def __str__(self):
        return self.konten
