from rest_framework import serializers
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio
from order.models import Order
from akun.models import Akun


class AkunSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'password')
        model = Akun


class ArtikelSerializer(serializers.ModelSerializer):
    komentar = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'penulis', 'judul', 'konten', 'publikasi', 'komentar')
        model = Artikel


class KomentarSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'artikel', 'member', 'konten', 'publikasi')
        model = Komentar


class PaketTerapiSerializer(serializers.ModelSerializer):
    audio = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'nama', 'deskripsi', 'harga', 'audio')
        model = PaketTerapi


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'paket_terapi', 'nama',
                  'filename', 'file', 'keterangan')
        model = Audio


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'pesan', 'bukti_path', 'tanggal_bayar',
                  'rek_pemesan', 'bank_pemesan', 'an_pemesan', 'rek_tujuan',
                  'jumlah', 'member', 'paket_terapi',
                  )
        model = Order
