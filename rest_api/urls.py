from django.urls import path
import rest_api.views as rv


urlpatterns = [
    # url for article module
    path('artikel_list', rv.ArtikelList.as_view()),
    path('artikel_load/<int:id>', rv.ArtikelLoad.as_view()),

    # url for member module
    path('member_load/<int:id>', rv.MemberLoad.as_view()),
    path('member_update/<int:pk>', rv.MemberUpdate.as_view()),

    # url for comment module
    path('komentar_load/<int:id>', rv.KomentarLoad.as_view()),
    # path('komentar_add/<int:artikel_id>/<int:member_id>', rv.KomentarAdd.as_view()),
    path('komentar_add', rv.KomentarAdd.as_view()),

    # url for Hypnotherapy module
    path('paket_terapi_list', rv.PaketTerapiList.as_view()),
    path('paket_terapi_load/<int:id>', rv.PaketTerapiLoad.as_view()),
    path('audio_list/<int:id>', rv.AudioLoad.as_view()),

    # url for order module
    path('order_add', rv.OrderAdd.as_view()),

    # url for account module
    path('akun_add', rv.AkunAdd.as_view()),
    # path('verifikasi_akun/<int:pk>', rv.VerifikasiAkun.as_view()),
    path('verifikasi_akun', rv.VerifikasiAkun.as_view()),
    path('forget_pass', rv.ForgetPass.as_view()),
    path('reset_pass', rv.ResetPass.as_view()),
    path('member_login/<str:email>/<str:password>', rv.MemberLogin.as_view()),
]
