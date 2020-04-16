from django.db import models

# Create your models here.


class PaketTerapi(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    aktif = models.BooleanField()
    mulai = models.DateField()
    akhir = models.DateField()
    publikasi = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'paket_terapi'

    def __str__(self):
        return self.nama


class Audio(models.Model):
    paket_terapi = models.ForeignKey(
        PaketTerapi, related_name='audio', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    filename = models.TextField(null=True)
    file = models.FileField(null=True, upload_to='./hypno/static/audio/')
    keterangan = models.TextField(null=True)

    class Meta:
        db_table = 'audio'

    def __str__(self):
        return self.nama
