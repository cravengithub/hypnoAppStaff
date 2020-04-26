from django.urls import path
import rest_api.views as rv

urlpatterns = [
    path('artikel_list', rv.ArtikelList.as_view()),
    path('artikel_load/<int:id>', rv.ArtikelLoad.as_view()),
    path('member_load/<int:id>', rv.MemberLoad.as_view()),
    path('member_update/<int:pk>', rv.MemberUpdate.as_view()),
    path('komentar_load/<int:id>', rv.KomentarLoad.as_view()),
    # path('komentar_add/<int:artikel_id>/<int:member_id>', rv.KomentarAdd.as_view()),
    path('komentar_add', rv.KomentarAdd.as_view()),
    path('paket_terapi_list', rv.PaketTerapiList.as_view()),
    path('paket_terapi_load/<int:id>', rv.PaketTerapiLoad.as_view()),
    path('audio_list/<int:id>', rv.AudioLoad.as_view()),
    path('order_add', rv.OrderAdd.as_view()),
    path('akun_add', rv.AkunAdd.as_view()),
    path('akun_load/<str:email>/<str:password>', rv.AkunLoad.as_view()),
]

