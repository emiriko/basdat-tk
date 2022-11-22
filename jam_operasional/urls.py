from django.urls import path
from .views import *

app_name = 'jam_operasional'

urlpatterns = [
    path('buat/', jam_operasional_buat, name='jam_operasional_buat'),
    path('daftar/', jam_operasional_daftar, name='jam_operasional_daftar'),
    path('ubah/<int:id>/', jam_operasional_ubah, name='jam_operasional_ubah'),
    path('hapus/<int:id>/', jam_operasional_hapus, name='jam_operasional_hapus'),
]