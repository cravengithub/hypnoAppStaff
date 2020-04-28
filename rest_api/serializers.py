from rest_framework import serializers
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio
from order.models import Order
from akun.models import Akun


class AkunSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'password', 'verification_code', 'nama')
        model = Akun


class VerifikasiAkunSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'verification_code')
        model = Akun


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nama', 'foto_src', 'kota_domisili', 'alamat', 'tanggal_lahir',
                  'jenis_kelamin', 'email', 'tempat_lahir', 'no_telepon')
        model = Akun


class ArtikelSerializer(serializers.ModelSerializer):
    # komentar = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'penulis', 'judul', 'konten', 'publikasi', 'ikon_src')
        model = Artikel


class KomentarSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()

    # artikel_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # member_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'member', 'konten', 'publikasi')
        # fields ="__all__"
        model = Komentar


class KomentarPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'member', 'artikel', 'konten')
        model = Komentar


class PaketTerapiSerializer(serializers.ModelSerializer):
    # audio = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ('id', 'nama', 'deskripsi', 'harga', 'ikon_src')
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
