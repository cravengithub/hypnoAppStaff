from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_audio/<int:id_pk>/<int:id_ad>',
         views.delete_audio, name='delete_audio'),
    path('upload/<int:id>', views.upload, name='upload'),
]
