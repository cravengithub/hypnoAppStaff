from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio
from order.models import Order
from akun.models import Akun
from .serializers import ArtikelSerializer, KomentarSerializer, PaketTerapiSerializer, AudioSerializer, OrderSerializer, AkunSerializer

# Create your views here.


class ArtikelList(generics.ListAPIView):
    queryset = Artikel.objects.filter(aktif=True)
    serializer_class = ArtikelSerializer


class KomentarLoad(APIView):
    def get(self, request, id, format=None):
        ar = Artikel.objects.get(id=id)
        komentar = Komentar.objects.filter(artikel=ar)
        serilizer = KomentarSerializer(komentar, many=True)
        return Response(serilizer.data)


class AkunAdd(generics.CreateAPIView):
    queryset = Akun.objects.filter(aktif=True)
    serializer_class = AkunSerializer


class AkunLoad(APIView):
    def get(self, request, email, password, format=None):
        akun = Akun.objects.filter(email=email, password=password)
        serilizer = AkunSerializer(akun, many=True)
        return Response(serilizer.data)


class KomentarAdd(generics.CreateAPIView):
    queryset = Komentar.objects.filter(aktif=True)
    serializer_class = KomentarSerializer


class PaketTerapiList(generics.ListAPIView):
    queryset = PaketTerapi.objects.filter(aktif=True)
    serializer_class = PaketTerapiSerializer


class AudioLoad(APIView):
    def get(self, request, id, format=None):
        pt = PaketTerapi.objects.get(id=id)
        audio = Audio.objects.filter(paket_terapi=pt)
        serilizer = AudioSerializer(audio, many=True)
        return Response(serilizer.data)


class OrderAdd(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
