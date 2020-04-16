from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('out', views.logout, name='logout'),
    path('forget', views.forget, name='forget'),
]
