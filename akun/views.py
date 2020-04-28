from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AkunForm
from .models import Akun

# Create your views here.


def index(request):
    akun = Akun.objects.all()
    context = {
        'akun': akun,
        'view': 'akun',
        'title': 'Member',
    }
    return render(request, 'akun/index.html', context)


def add(request):
    if request.method == 'POST':
        form = AkunForm(request.POST)
        sex_flag = request.POST.get('jenis_kelamin')
        aktif_flag = request.POST.get('aktif')
        form.fields['jenis_kelamin'].choices = [(sex_flag, sex_flag)]
        form.fields['aktif'].choices = [(aktif_flag, aktif_flag)]
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Data member berhasil disimpan.')
            return redirect('/akun')
        else:
            messages.add_message(request, messages.ERROR,
                                 form.errors)
    else:
        form = AkunForm()
    context = {
        'title': 'Member -> Input Data',
        'form': form,
        'view': 'akun',
    }
    return render(request, 'akun/form.html', context)


def profile(request, id):
    akun = Akun.objects.get(id=id)
    context = {
        'title': 'Member -> Profil',
        'akun': akun,
        'view': 'akun',
    }
    return render(request, 'akun/profil.html', context)


def edit(request, id):
    akun = Akun.objects.get(id=id)
    form = AkunForm(instance=akun)
    form.fields['jenis_kelamin'].initial = [akun.jenis_kelamin]
    form.fields['aktif'].initial = [akun.aktif]
    form.fields['verification'].initial = [akun.verification]
    if request.method == 'POST':
        form = AkunForm(request.POST or None, instance=Akun.objects.get(id=id))
        sex_flag = request.POST.get('jenis_kelamin')
        aktif_flag = request.POST.get('aktif')
        ver_flag = request.POST.get('verification')
        foto = request.POST.get('foto_src')
        # print(foto)
        form.fields['jenis_kelamin'].choices = [(sex_flag, sex_flag)]
        form.fields['aktif'].choices = [(ver_flag, ver_flag)]

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Data member berhasil diubah.')
            return redirect('/akun')
        else:
            # print(50*'*')
            messages.add_message(request, messages.ERROR,
                                 form.errors)
    context = {
        'title': 'Member -> Ubah Data',
        'form': form,
        'view': 'akun',
    }
    return render(request, 'akun/form.html', context)


def delete(request, id):
    Akun.objects.get(id=id).delete()
    messages.add_message(request, messages.SUCCESS,
                         'Data member berhasil dihapus.')
    return redirect('/akun')
