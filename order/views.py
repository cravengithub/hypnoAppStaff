from django.shortcuts import render, redirect
from hypno.models import PaketTerapi
from akun.models import Akun
from .models import Order
from .forms import OrderForm
# Create your views here.


def index(request):
    order = Order.objects.all()
    context = {
        'order': order,
        'view': 'order',
        'title': 'Pemesanan Paket',
    }
    return render(request, 'order/index.html', context)


def add(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        member = Akun.objects.get(email=email)
        if member is not None:
            form = OrderForm(request.POST)
            id_pt = request.POST.get('paket_terapi')
            form.fields['paket_terapi'].choices = [(id_pt, id_pt)]
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.member = member
                new_form.paket_terapi = PaketTerapi.objects.get(id=id_pt)
                new_form.save()
                return redirect('/order')
            else:
                print(50*'*')
                print(form.errors)
    else:
        form = OrderForm()
    context = {
        'view': 'order',
        'title': 'Pemesanan Paket -> Input Data',
        'form': form
    }
    return render(request, 'order/form.html', context)


def edit(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    form.fields['email'].initial = order.member.email
    if request.method == 'POST':
        form = OrderForm(request.POST or None,
                         instance=Order.objects.get(id=id))
        id_pt = request.POST.get('paket_terapi')
        form.fields['paket_terapi'].choices = [(id_pt, id_pt)]
        member = Akun.objects.get(email=order.member.email)
        if member is not None:
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.member = member
                new_form.paket_terapi = PaketTerapi.objects.get(id=id_pt)
                new_form.save()
                return redirect('/order')
            else:
                print(50*'*')
                print(form.errors)
    context = {
        'order': order,
        'view': 'order',
        'title': 'Pemesanan Paket -> Ubah Data',
        'form': form
    }
    return render(request, 'order/form.html', context)


def delete(request, id):
    Order.objects.get(id=id).delete()
    return redirect('/order')
