from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArtikelForm, KomentarForm
from .models import Artikel, Komentar
from akun.models import Akun


# Create your views here.


def index(request):
    artikel = Artikel.objects.all()
    context = {
        'view': 'artikel',
        'title': 'Artikel dan Komentar',
        'artikel': artikel,
    }
    return render(request, 'artikel/index.html', context)


def add(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST)
        aktif_flag = request.POST.get('aktif')
        form.fields['aktif'].choices = [(aktif_flag, aktif_flag)]
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Data artikel berhasil disimpan.')
            return redirect('/artikel')
        else:
            messages.add_message(request, messages.ERROR,
                                 form.errors)
    else:
        form = ArtikelForm()
    context = {
        'view': 'artikel',
        'title': 'Artikel dan Komentar -> Input Data',
        'form': form,
    }
    return render(request, 'artikel/form.html', context)


def detail(request, id):
    artikel = Artikel.objects.get(id=id)
    akun = Akun.objects.filter(status='staf').first()
    # akun = Akun.objects.get(id=3)
    komen = Komentar.objects.filter(artikel=artikel)
    if request.method == 'POST':
        km = Komentar()
        km.member = akun
        km.artikel = artikel
        form = KomentarForm(request.POST or None, instance=km)
        if form.is_valid():
            form.save()
            path = '/artikel/detail/' + str(id)
            return redirect(path)
    else:
        form = KomentarForm()
    context = {
        'view': 'artikel',
        'title': 'Artikel dan Komentar -> Detail Data',
        'artikel': artikel,
        'komentar': komen,
        'form': form,
    }
    # print(akun.nama)
    # print(artikel.konten, 50*'---')
    return render(request, 'artikel/detail.html', context)


def edit(request, id):
    artikel = Artikel.objects.get(id=id)
    form = ArtikelForm(instance=artikel)
    form.fields['aktif'].initial = [artikel.aktif]
    if request.method == 'POST':
        form = ArtikelForm(request.POST or None,
                           instance=Artikel.objects.get(id=id))
        # print(form)
        aktif_flag = request.POST.get('aktif')
        form.fields['aktif'].choices = [(aktif_flag, aktif_flag)]
        # print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Data artikel berhasil diubah.')
            return redirect('/artikel')
        else:
            # print(50*'*')
            messages.add_message(request, messages.ERROR,
                                 form.errors)
    context = {
        'view': 'artikel',
        'title': 'Artikel dan Komentar -> Input Data',
        'artikel': artikel,
        'form': form,
    }
    return render(request, 'artikel/form.html', context)


def delete(request, id):
    Artikel.objects.get(id=id).delete()
    messages.add_message(request, messages.SUCCESS,
                         'Data artikel berhasil dihapus.')
    return redirect('/artikel')


def delete_comment(request, id):
    comment = Komentar.objects.get(id=id)
    id_artikel = comment.artikel.id
    comment.delete()
    path = '/artikel/detail/'+str(id_artikel)
    return redirect(path)


def comment(request, id):
    comment = Komentar.objects.get(id=id)
    if comment.aktif:
        comment.aktif = False
    else:
        comment.aktif = True
    comment.save()
    path = '/artikel/detail/'+str(comment.artikel.id)
    return redirect(path)
