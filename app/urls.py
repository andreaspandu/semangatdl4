from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('createdata', views.createdata, name ='createdata'),
    path('bikinlayanan', views.bikinlayanan, name ='bikinlayanan'),
    path('bikinpaket', views.bikinpaket, name ='bikinpaket'),
    path('hapus/<str:id>', views.hapus, name="hapus"),
    path('perbarui/<str:id>', views.perbarui, name ='perbarui')
]   