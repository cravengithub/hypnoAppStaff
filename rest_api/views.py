from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from artikel.models import Artikel, Komentar
from hypno.models import PaketTerapi, Audio
from order.models import Order
from akun.models import Akun
from django.core import signing
import base64 as bs
from random import randint
from django.conf import  settings
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from .serializers import ArtikelSerializer, KomentarSerializer, \
    PaketTerapiSerializer, AudioSerializer, OrderSerializer, \
    AkunSerializer, MemberSerializer, KomentarPostSerializer, \
    VerifikasiAkunSerializer


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
    message = None
    serializer = None
    status = None

    def perform_create(self, serializer):  # prevent changing the course that is being reviewed
        message = ''
        # akun = get_object()
        code = randint(10000, 99999);
        # akun.verification_code = code
        # serializer.save(Akun = akun)
        # serializer.data['password'] = signing.dumps(serializer.data['password'])
        data = serializer.data
        chiper = signing.dumps(data['password'])
        chiper64 = bs.b64encode(chiper.encode())
        data['password'] = chiper64.decode()
        data['verification_code'] = code
        serializer = AkunSerializer(data=data)
        self.serializer = serializer
        # print(akun)
        # print(serializer)
        akun = Akun.objects.filter(email=data['email'])
        if len(akun) < 1:
            if serializer.is_valid():
                serializer.save()
                recipient = data['email']
                # from_email = 'hypnotherapyapplication@gmail.com'
                from_email = settings.EMAIL_HOST_USER
                # subject = '[NO REPLY] Verifikasi Akun Pengguna'
                subject = settings.ACCOUNT_VERIFICATION_SUBJECT
                # message_html = '''<p>Selamat Anda terlah terdaftar sebagai pengguna <strong>HypnoSession Mobile App</strong>.\n
                # Selanjutnya, lakukan verifikasi pengguna dengan memasukkan kode sebagai berikut:\n
                # ''' + '<br/><strong>' + str(code) + '</strong></p>'
                message_html = settings.ACCOUNT_VERIFICATION_MESSAGE + '<strong>' + str(code) + '</strong>'
                try:
                    send_mail(subject, message_html, from_email, [recipient], html_message=message_html)
                    self.message = 'Kode Verifikasi telah dikirimkan ke email.'
                    self.status = 1
                    # print(self.message)
                except BadHeaderError:
                    message = 'Invalid header found.'
                    # print(self.message)
                    self.status = 0
        else:
            self.status = 2
            self.message = 'Email yang Anda gunakan untuk registrasi telah terdaftar. Apabila lupa password dapat gunakan fitur yang tersedia.'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # self.message += '''
        #                 \nDescripton of status:
        #                 \n0 : error
        #                 \n1 : Success registering
        #                 \n2 : Email have been existed
        #                 '''
        return Response({
            # 'data': self.serializer.data,
            'errors': self.serializer.error_messages,
            'message': self.message,
            'status': self.status,
            'result': 'OK'
        })


class VerifikasiAkun(generics.CreateAPIView):
    queryset = Akun.objects.all()
    serializer_class = VerifikasiAkunSerializer
    message = None
    serializer = None
    status = None
    data = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': self.message,
            'status': self.status,
            'data': self.data
        })

    def perform_create(self, serializer):
        data = self.request.data
        aks = Akun.objects.filter(Q(email=data['email']) & Q(verification_code=data['verification_code']))
        if len(aks) > 0:
            self.message = "Akun pengguna telah diverifikasi dan siap menggunakan Aplikasi HypnoSession."
            member = aks.first()
            # member = Akun.objects.get(id=mb.id)
            self.data = {
                'id': member.id,
                'email': member.email,
            }
            member.verification = True
            member.save()
            # print(member.email, ":", member.verification)
            self.status = 1
            # self.message = "Proses verifikasi pengguna berhasil"
        else:
            self.message = "Kode Verifikasi dan email tidak sesuai"
            self.status = 0


'''
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': self.message,
            'status': self.status
        })
        '''


class MemberLogin(APIView):
    def get(self, request, email, password, format=None):
        # print(Akun.objects.filter(email=email).query)
        aks = Akun.objects.filter(email=email)
        if len(aks) > 0:
            ak = aks.first()
            chiperEncode = bs.b64decode(ak.password)
            chiper = chiperEncode.decode()
            key = signing.loads(chiper)
            # print(ak.email)
            if key == password:
                data = {
                    'id': ak.id,
                    'email': ak.email
                }

                serilizer = AkunSerializer(data=data)
                serilizer.is_valid()
                return Response(data)
        return Response(None)


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


class ForgetPass(generics.CreateAPIView):
    queryset = Akun.objects.all()
    serializer_class = AkunSerializer
    message = None
    serializer = None
    status = None
    data = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': self.message,
            'status': self.status,
            'data': self.data
        })

    def perform_create(self, serializer):
        data = self.request.data
        aks = Akun.objects.filter(email=data['email'])
        if len(aks) > 0:
            code = randint(10000, 99999)
            member = aks.first();
            member.verification_code = code
            member.save()
            self.data={
                'id':member.id,
                'email':member.email,
                # 'verification_code':member.verification_code
            }
            recipient = data['email']
            # from_email = 'hypnotherapyapplication@gmail.com'
            from_email = settings.EMAIL_HOST_USER
            # subject = '[NO REPLY] Kode Reset Password Pengguna'
            subject = '[NO REPLY] Kode Reset Password Pengguna'
            # message_html = '''<p>Ini merupakan layanan untuk Reset Password. Selanjutnya, lakukan verifikasi pengguna dengan memasukkan kode sebagai berikut:\n
            #                     ''' + '<br/><strong>' + str(code) + '</strong></p>'
            message_html = settings.FORGET_PASSWORD_MESSAGE+'<strong>' + str(code) + '</strong>'
            try:
                send_mail(subject, message_html, from_email, [recipient], html_message=message_html)
                self.message = 'Kode Reset Password telah dikirimkan ke email.'
                self.status = 1
                # print(self.message)
            except BadHeaderError:
                message = 'Invalid header found.'
                # print(self.message)
                self.status = 0

        else:
            self.message = "Email tidak ditemukan."
            self.status = 0


'''
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': self.message,
            'status': self.status
        })
'''





class ResetPass(generics.CreateAPIView):
    queryset = Akun.objects.all()
    serializer_class = AkunSerializer
    message = None
    serializer = None
    status = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': self.message,
            'status': self.status
        })
    def perform_create(self, serializer):
        data = self.request.data
        aks = Akun.objects.filter(Q(email=data['email']) & Q(verification_code=data['verification_code']))
        if len(aks) > 0:
            member = aks.first();
            chiper = signing.dumps(data['password'])
            # print(self.request.data, 50*'#')
            chiper64 = bs.b64encode(chiper.encode())
            member.password = chiper64.decode()
            member.save()
            recipient = data['email']
            # from_email = 'hypnotherapyapplication@gmail.com'
            from_email = settings.EMAIL_HOST_USER
            # subject = '[NO REPLY] Perubahan Password Pengguna'
            subject = settings.RESET_PASSWORD_MOBILE_SUBJECT
            # message_html = 'Proses perubahan Password yang Anda lakukan telah berhasil.'
            message_html = settings.RESET_PASSWORD_MOBILE_MESSAGE
            try:
                send_mail(subject, message_html, from_email, [recipient], html_message=message_html)
                self.message = 'Proses perubahan password telah berhasil.'
                self.status = 1
                print(self.message)
            except BadHeaderError:
                message = 'Invalid header found.'
                print(self.message)
                self.status = 0

        else:
            self.message = "Kode Reset Password atau email tidak sesuai"
            self.status = 0
'''
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': self.message,
            'status': self.status
        })
'''

