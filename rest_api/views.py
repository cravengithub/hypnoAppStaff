from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio
from order.models import Order
from akun.models import Akun
from .serializers import ArtikelSerializer, KomentarSerializer, \
    PaketTerapiSerializer, AudioSerializer, OrderSerializer, \
    AkunSerializer, MemberSerializer, KomentarPostSerializer


# Create your views here.


class ArtikelList(generics.ListAPIView):
    queryset = Artikel.objects.filter(aktif=True)
    serializer_class = ArtikelSerializer


class ArtikelLoad(APIView):
    def get(self, request, id, format=None):
        ar = Artikel.objects.get(id=id)
        serilizer = ArtikelSerializer(ar)
        return Response(serilizer.data)


class KomentarLoad(APIView):
    def get(self, request, id, format=None):
        ar = Artikel.objects.get(id=id)
        komentar = Komentar.objects.filter(artikel=ar)
        serilizer = KomentarSerializer(komentar, many=True)
        return Response(serilizer.data)


class KomentarAdd(generics.CreateAPIView):
    queryset = Komentar.objects.filter(aktif=True)
    serializer_class = KomentarPostSerializer


class AkunAdd(generics.CreateAPIView):
    queryset = Akun.objects.filter(aktif=True)
    serializer_class = AkunSerializer


class AkunLoad(APIView):
    def get(self, request, email, password, format=None):
        akun = Akun.objects.filter(email=email, password=password)
        serilizer = AkunSerializer(akun, many=True)
        return Response(serilizer.data)


class MemberUpdate(generics.UpdateAPIView):
    queryset = Akun.objects.filter(aktif=True)
    serializer_class = MemberSerializer


class MemberLoad(APIView):
    def get(self, request, id, format=None):
        mb = Akun.objects.get(id=id)
        serilizer = MemberSerializer(mb)
        return Response(serilizer.data)

    # def post(self, request,artikel_id, member_id, format=None):
    #     memberx = Akun.objects.get(id=member_id)
    #     artikelx = Artikel.objects.get(id=artikel_id)
    #     km = Komentar.objects.filter(aktif=True, member = memberx, artikel = artikelx)
    #     serilizer = KomentarSerializer(km)
    #     return Response(serilizer.data)


class PaketTerapiList(generics.ListAPIView):
    queryset = PaketTerapi.objects.filter(aktif=True)
    serializer_class = PaketTerapiSerializer


class PaketTerapiLoad(APIView):
    def get(self, request, id, format=None):
        pt = PaketTerapi.objects.get(id=id)
        serilizer = PaketTerapiSerializer(pt)
        return Response(serilizer.data)


class AudioLoad(APIView):
    def get(self, request, id, format=None):
        pt = PaketTerapi.objects.get(id=id)
        audio = Audio.objects.filter(paket_terapi=pt)
        serilizer = AudioSerializer(audio, many=True)
        return Response(serilizer.data)


class OrderAdd(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
