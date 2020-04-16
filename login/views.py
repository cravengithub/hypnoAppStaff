from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import base64 as bs
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def index(request):
    if request.method == 'POST':
        username_email = request.POST.get('email')
        password = request.POST.get('password')

        auth = None
        try:
            user = User.objects.get(email=username_email)
            auth = authenticate(
                request, username=user.username, password=password)
        except Exception as e:
            print(e)
        try:
            user = User.objects.get(username=username_email)
            auth = authenticate(
                request, username=user.username, password=password)
        except Exception as e:
            print(e)

        if auth is not None:
            login(request, user)
            return redirect('/beranda')
        else:
            messages.add_message(request, messages.ERROR,
                                 'username atau password tidak sesuai')

    return render(request, 'login/signin.html')


def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user is not None:
            # send mail to recipient
            recipient = user.email
            from_email = 'hypnotherapyapplication@gmail.com'
            subject = '[NO REPLY] Konfirmasi Reset Password'
            message = '''Terima kasih telah menggunakan layanan ini.
            \nLayanan ini digunakan untuk me-reset password apabila pengguna lupa passwordnya.
            \nBerikut ini terdapat alamat url untuk melakukan reset password:\n'''
            base = bs.b64encode(email.encode())
            url = 'http://localhost:8000/login/reset/' + base.decode()
            message += url
            # print(str(base))
            back = bs.b64decode(base)
            try:
                send_mail(subject, message, from_email, [recipient])
                messages.add_message(request, messages.SUCCESS,
                                     'Verifikasi Reset Password telah dikirimkan ke email.')
            except BadHeaderError:
                messages.add_message(request, messages.ERROR,
                                     'Invalid header found.')
            return redirect('/login')
    return render(request, 'login/forget.html')


def logout(request):
    return redirect('/login/')
