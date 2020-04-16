from django.shortcuts import render
from akun.models import Akun
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio

# Create your views here.


def index(request):
    total_akun = Akun.objects.count()
    total_artikel = Artikel.objects.count()
    total_Komentar = Komentar.objects.count()
    total_paket = PaketTerapi.objects.count()
    total_audio = Audio.objects.count()

    context = {
        'title': 'Beranda',
        'akun': total_akun,
        'artikel': total_artikel,
        'komentar': total_Komentar,
        'paket': total_paket,
        'audio': total_audio,
        'view': 'beranda',
    }
    return render(request, 'beranda/index.html', context)
