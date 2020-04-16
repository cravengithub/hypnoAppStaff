from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PaketTerapiForm, AudioForm
from .models import PaketTerapi, Audio
import datetime
import os

# Create your views here.


def index(request):
    paket = PaketTerapi.objects.all()
    context = {
        'paket': paket,
        'view': 'hypno',
        'title': 'Paket Hypnotherapy',
    }
    return render(request, 'hypno/index.html', context)


def add(request):
    if request.method == 'POST':
        form = PaketTerapiForm(request.POST)
        aktif_flag = request.POST.get('aktif')
        form.fields['aktif'].choices = [(aktif_flag, aktif_flag)]
        if form.is_valid():
            form.save()
            return redirect('/hypno')
        else:
            print(50*'*')
            print(form.errors)
    else:
        form = PaketTerapiForm()
    paket = PaketTerapi.objects.all()
    context = {
        'paket': paket,
        'view': 'hypno',
        'title': 'Paket Hypnotherapy -> Input Data',
        'form': form
    }
    return render(request, 'hypno/form.html', context)


def edit(request, id):
    paket = PaketTerapi.objects.get(id=id)
    form = PaketTerapiForm(instance=paket)
    form.fields['aktif'].initial = [paket.aktif]
    if request.method == 'POST':
        form = PaketTerapiForm(request.POST or None,
                               instance=PaketTerapi.objects.get(id=id))
        aktif_flag = request.POST.get('aktif')
        form.fields['aktif'].choices = [(aktif_flag, aktif_flag)]
        if form.is_valid():
            try:
                form.save()
                return redirect('/hypno')
            except (ValueError, TypeError):
                print(ValueError)
                pass
        else:
            print(50*'*')
            print(form.errors)
    context = {
        'paket': paket,
        'view': 'hypno',
        'title': 'Paket Hypnotherapy -> Ubah Data',
        'form': form
    }
    return render(request, 'hypno/form.html', context)


def delete(request, id):
    PaketTerapi.objects.get(id=id).delete()
    return redirect('/hypno')


def delete_audio(request, id_pk, id_ad):
    audio = Audio.objects.get(id=id_ad)
    audio.delete()
    # if audio.file is not None:
    # if os.path.isfile(audio.file):
    # os.remove(audio.file.path)
    # print(id_ad, 50*'%')
    return redirect('/hypno/upload/'+str(id_pk))


def upload(request, id):
    paket = PaketTerapi.objects.get(id=id)
    audio = Audio.objects.filter(paket_terapi=paket)
    form = AudioForm()
    if request.method == 'POST':
        audioForm = AudioForm(request.POST or None, request.FILES)
        if audioForm.is_valid():
            ad = audioForm.save(commit=False)
            # strdatetime = str(datetime.datetime.today()).replace(' ', '=')
            # ad.file = 'hypno/static/audio/'+strdatetime+'-audio.mp3'
            files = request.FILES['file']
            ad.filename = files.name
            ad.paket_terapi = paket
            # ad.path = '/hypno/static/audio/' + filename
            ad.save()
            return redirect('/hypno/upload/'+str(id))
        else:
            print(50*'*')
            print(form.errors)

    context = {
        'paket': paket,
        'view': 'hypno',
        'title': 'Paket Hypnotherapy -> Unggah Audio',
        'form': form,
        'audio': audio,
    }

    return render(request, 'hypno/upload.html', context)


def __handle_uploaded_file(f):
    strdatetime = str(datetime.datetime.today()).replace(' ', '|')
    # print(strdate, 50*'x')
    filename = strdatetime + '-' + f.name
    with open('./hypno/static/audio/'+filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename
